import requests


def test_get_active_companies():
    url = "http://5.101.50.27:8000/company/list"

    # Отправляем GET-запрос
    response = requests.get(url)

    # Проверяем, что сервер вернул статус 200
    assert response.status_code == 200, f"Ошибка: статус {response.status_code}"
    # Преобразуем JSON-ответ в список словарей
    companies = response.json()

    # Фильтруем только активные компании
    active_companies = [company for company in companies if company["is_active"]]

    # Проверяем, что активных компаний не меньше 3
    assert len(active_companies) >= 3, f"Ожидалось >=3 активных компаний, но найдено {len(active_companies)}"

    print(f"Тест пройден! Найдено {len(active_companies)} активных компаний.")
