import pytest
from booker_api import BookerApi

BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture
def api():
    """
    Инициализирует и возвращает экземпляр клиентского класса BookerApi,
    сконфигурированный базовым URL-адресом целевого сервиса.
    """
    return BookerApi(BASE_URL)


@pytest.fixture
def sample_booking():
    """
    Формирует и возвращает эталонный набор валидных данных бронирования
    для использования в качестве базовой полезной нагрузки (payload) в тестах.
    """
    return {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-08-01",
            "checkout": "2026-08-10"
        },
        "additionalneeds": "Breakfast"
    }


def test_partial_update_additionalneeds_only(api, sample_booking):
    """
    Положительный сценарий: Проверка частичного обновления через метод HTTP PATCH.

    Цель теста:
    Верификация изолированного изменения отдельного опционального строкового поля
    и проверка сохранения целостности остальных данных объекта.

    Критерии успешности (Assertions):
    1. Возврат сервером HTTP-статуса 200 OK.
    2. Успешное изменение значения целевого поля 'additionalneeds'.
    3. Сохранение исходных значений неизменяемых полей ('firstname', 'lastname').
    """
    # Создание тестовой сущности бронирования
    created = api.create_booking(sample_booking)
    booking_id = created["bookingid"]

    # Генерация токена доступа администратора
    token = api.get_auth_token("admin", "password123")

    # Формирование дельты обновлений (только одно поле)
    patch_payload = {
        "additionalneeds": "Vegetarian Diet"
    }

    # Выполнение частичного обновления сущности
    resp = api.partial_update_booking(booking_id, patch_payload, token)
    assert resp.status_code == 200

    # Валидация измененных и неизмененных атрибутов в ответе
    patched_data = resp.json()
    assert patched_data["additionalneeds"] == "Vegetarian Diet"
    assert patched_data["firstname"] == sample_booking["firstname"]
    assert patched_data["lastname"] == sample_booking["lastname"]


def test_delete_booking_with_invalid_token(api, sample_booking):
    """
    Отрицательный сценарий: Валидация границ безопасности и авторизации.

    Цель теста:
    Проверка устойчивости системы управления доступом API при попытке
    удаления существующей сущности с передачей некорректного токена.

    Критерии успешности (Assertions):
    1. Возврат сервером HTTP-статуса 403 Forbidden.
    2. Блокировка критической мутации (удаления) данных на стороне бэкенда.
    """
    # Создание целевой сущности бронирования для удаления
    created = api.create_booking(sample_booking)
    booking_id = created["bookingid"]

    # Инициализация заведомо невалидного токена авторизации
    invalid_token = "invalid_token_12345"

    # Попытка удаления записи без надлежащих прав доступа
    resp = api.delete_booking(booking_id, invalid_token)

    # Ожидаемый результат: доступ запрещен (403)
    assert resp.status_code == 403
