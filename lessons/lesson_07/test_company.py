from company_api import CompanyApi  # Импортируем класс


# **Тест: проверка увеличения списка компаний после создания**
base_url = "http://5.101.50.27:8000"

def test_create_company_increases_count():
    """Тест: создание компании увеличивает список компаний на 1"""

    api = CompanyApi(base_url)  # Инициализация API-клиента
    # 1. Получаем текущий список компаний
    companies_before = api.get_company_list()
    initial_count = len(companies_before) #10

    # 2. Создаём новую компанию
    api.create_company(name="Test Company", description="Automated test creation")
    # 3. Повторно получаем список компаний
    companies_after = api.get_company_list()
    final_count = len(companies_after) #11

    # 4. Проверяем, что длина списка увеличилась на 1
    assert final_count == initial_count + 1, f"Ожидалось {initial_count + 1} компаний, найдено {final_count}"
    print(f"Тест пройден: до {initial_count}, после {final_count} (добавлена 1 компания).")

def test_get_one_company():
    # base_url = "http://5.101.50.27:8000"
    api = CompanyApi(base_url)
    # Создаем компанию
    name = "PyCharm"
    descr = "IDE"
    result = api.create_company(name, descr)
    new_id = result["id"]
    # Обращаемся к компании
    new_company = api.get_company(new_id)
    # Проверим название, описание и статус новой компании:
    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["is_active"] is True

def test_delete_company():
    """Тест: удаление компании"""

    # base_url = "http://5.101.50.27:8000"
    api = CompanyApi(base_url)
    # 1. Создаём компанию
    name = "Company to be deleted"
    descr = "Delete me"
    result = api.create_company(name, descr)
    company_id = result["id"]
    # 2. Получаем компанию по ID
    new_company = api.get_company(company_id)

    # 3. Проверяем, что компания создана корректно
    assert new_company["name"] == name, f"Ожидалось '{name}', получено '{new_company['name']}'"
    assert new_company["description"] == descr, f"Ожидалось '{descr}', получено '{new_company['description']}'"
    assert new_company["is_active"] is True, "Ожидалось, что компания активна"
    # 4. Получаем список компаний и запоминаем количество
    companies_before = api.get_company_list()
    len_before = len(companies_before)

    # 5. Удаляем компанию
    api.delete_company(company_id, 'harrypotter', 'expelliarmus')
    # 6. Получаем список компаний после удаления
    companies_after = api.get_company_list()
    len_after = len(companies_after)

    # 7. Проверяем, что список компаний уменьшился на 1
    assert len_before - len_after == 1, f"Ожидалось {len_before - 1} компаний, найдено {len_after}"
    # 8. Проверяем, что удалённая компания больше не доступна
    deleted = api.get_company(company_id)
    assert deleted["detail"] == "Компания не найдена", f"Ожидалось 'Компания не найдена', получено '{deleted['detail']}'"

    print(f"Тест пройден: компания {company_id} успешно удалена.")

def test_deactivate_company():
    """Тест: деактивация компании"""

    # base_url = "http://5.101.50.27:8000"
    api = CompanyApi(base_url)
    # 1. Создаём компанию
    name = "Company to be deactivated"
    result = api.create_company(name)
    company_id = result["id"]

    # 2. Деактивируем компанию
    body = api.set_active_state(company_id, False, 'harrypotter', 'expelliarmus')
    # 3. Проверяем, что статус изменился на "неактивный"
    assert body["is_active"] is False, "Ожидалось, что компания будет неактивной"

    print(f"Тест пройден: компания {company_id} успешно деактивирована.")

# Запуск теста
# test_create_company_increases_count()
