import pytest
from booker_api import BookerApi

BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture
def api():
    return BookerApi(BASE_URL)


@pytest.fixture
def auth_token(api):
    """Фикстура для получения токена перед тестами, требующими прав"""
    return api.get_auth_token("admin", "password123")


@pytest.fixture
def sample_booking():
    """Тестовые данные для создания брони"""
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


@pytest.fixture
def booking_lifecycle(api, auth_token, sample_booking):
    """
    Фикстура автоматического жизненного цикла бронирования.
    Создает бронь перед тестом и ГАРАНТИРОВАННО удаляет её после его окончания.
    """
    # [Setup]: Создаем бронирование до начала выполнения теста
    created_data = api.create_booking(sample_booking)
    booking_id = created_data["bookingid"]

    # Передаем управление и данные в сам тест
    yield created_data

    # [Teardown]: Выполняется автоматически ПОСЛЕ завершения теста
    api.delete_booking(booking_id, auth_token)


# ------------------- ТЕСТЫ -------------------

def test_user_authorization(api):
    """Тест: получение токена авторизации"""
    token = api.get_auth_token("admin", "password123")
    assert token is not None and len(token) > 0, "Токен не должен быть пустым"


def test_create_booking(booking_lifecycle, sample_booking):
    """Тест: создание бронирования и проверка сохраненных данных"""
    # Пользуемся бронью, созданной фикстурой
    created_data = booking_lifecycle

    assert "bookingid" in created_data
    assert created_data["booking"]["firstname"] == sample_booking["firstname"]
    assert created_data["booking"]["totalprice"] == sample_booking["totalprice"]


def test_get_booking_by_id(api, booking_lifecycle):
    """Тест: получение бронирования по ID"""
    created_data = booking_lifecycle
    booking_id = created_data["bookingid"]

    resp = api.get_booking(booking_id)
    assert resp.status_code == 200

    data = resp.json()
    assert data["firstname"] == "John"
    assert data["lastname"] == "Doe"


def test_full_update_booking(api, auth_token, booking_lifecycle):
    """Тест: полное изменение бронирования (PUT)"""
    created_data = booking_lifecycle
    booking_id = created_data["bookingid"]

    updated_payload = {
        "firstname": "John",
        "lastname": "Updated",
        "totalprice": 300,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-08-05",
            "checkout": "2026-08-15"
        },
        "additionalneeds": "Late Checkout"
    }

    resp = api.update_booking(booking_id, updated_payload, auth_token)
    assert resp.status_code == 200

    updated_data = resp.json()
    assert updated_data["lastname"] == "Updated"
    assert updated_data["totalprice"] == 300
    assert updated_data["depositpaid"] is False


def test_partial_update_booking(api, auth_token, booking_lifecycle, sample_booking):
    """Тест: частичное изменение бронирования (PATCH)"""
    created_data = booking_lifecycle
    booking_id = created_data["bookingid"]

    patch_payload = {
        "firstname": "Alexander",
        "totalprice": 500
    }

    resp = api.partial_update_booking(booking_id, patch_payload, auth_token)
    assert resp.status_code == 200

    patched_data = resp.json()
    assert patched_data["firstname"] == "Alexander"
    assert patched_data["totalprice"] == 500
    assert patched_data["lastname"] == sample_booking["lastname"]


def test_delete_booking(api, auth_token, sample_booking):
    """Тест: удаление бронирования (DELETE)"""
    created = api.create_booking(sample_booking)
    booking_id = created["bookingid"]

    # 1. Удаляем бронь
    delete_resp = api.delete_booking(booking_id, auth_token)

    # Проверяем, что код ответа либо 200, либо 201
    # Альтернативный вариант без квадратных скобок:
    assert delete_resp.status_code == 200 or delete_resp.status_code == 201, f"Ожидался статус 200/201, получен {delete_resp.status_code}"


    # 2. Проверяем, что бронь больше не находится по ID (статус 404)
    get_resp = api.get_booking(booking_id)
    assert get_resp.status_code == 404, "Удаленная бронь не должна быть найдена"


def test_filter_booking_by_name(api, sample_booking, auth_token):
    """Тест: фильтрация бронирования по имени"""
    booking_data = sample_booking.copy()
    booking_data["firstname"] = 'testfirstname'
    booking_data["lastname"] = 'testlastname'

    created = api.create_booking(booking_data)
    booking_id = created["bookingid"]

    try:
        params = {
            "firstname": 'testfirstname',
            "lastname": 'testlastname'
        }
        booking_ids = api.get_booking_ids(params)
        found_ids = [item["bookingid"] for item in booking_ids]
        assert booking_id in found_ids
    finally:
        # Ручной блок очистки, специфичный для этого теста модификации имен
        api.delete_booking(booking_id, auth_token)


def test_get_nonexistent_booking(api):
    """Тест: получение несуществующего бронирования по изолированному ID"""
    # Использование жестко заданного огромного числа гарантирует стабильный 404
    nonexistent_id = 999999999

    resp = api.get_booking(nonexistent_id)
    assert resp.status_code == 404, f"Ожидался статус 404, получен {resp.status_code}"


def test_create_proof(booking_lifecycle):
    """Тест: создание бронирования с проверкой структуры ответа"""
    created_booking = booking_lifecycle
    keys_std = ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates", "additionalneeds"]
    keys = list(created_booking['booking'].keys())

    for key in keys_std:
        assert key in keys, f"Ключ {key} отсутствует в ответе API"
