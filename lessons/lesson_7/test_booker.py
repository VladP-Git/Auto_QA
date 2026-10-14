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


# ------------------- ТЕСТЫ -------------------

def test_user_authorization(api):
    """Тест: получение токена авторизации"""
    token = api.get_auth_token("admin", "password123")
    assert token is not None and len(token) > 0, "Токен не должен быть пустым"


def test_create_booking(api, sample_booking):
    """Тест: создание бронирования и проверка сохраненных данных"""
    created_data = api.create_booking(sample_booking)

    assert "bookingid" in created_data
    assert created_data["booking"]["firstname"] == sample_booking["firstname"]
    assert created_data["booking"]["totalprice"] == sample_booking["totalprice"]


def test_get_booking_by_id(api, sample_booking):
    """Тест: получение бронирования по ID"""
    created = api.create_booking(sample_booking)
    booking_id = created["bookingid"]

    resp = api.get_booking(booking_id)
    assert resp.status_code == 200

    data = resp.json()
    assert data["firstname"] == "John"
    assert data["lastname"] == "Doe"


def test_full_update_booking(api, auth_token, sample_booking):
    """Тест: полное изменение бронирования (PUT)"""
    created = api.create_booking(sample_booking)
    booking_id = created["bookingid"]

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


def test_partial_update_booking(api, auth_token, sample_booking):
    """Тест: частичное изменение бронирования (PATCH)"""
    created = api.create_booking(sample_booking)
    booking_id = created["bookingid"]

    patch_payload = {
        "firstname": "Alexander",
        "totalprice": 500
    }

    resp = api.partial_update_booking(booking_id, patch_payload, auth_token)
    assert resp.status_code == 200

    patched_data = resp.json()
    # Проверяем измененные поля
    assert patched_data["firstname"] == "Alexander"
    assert patched_data["totalprice"] == 500
    # Проверяем, что нетронутые поля сохранили старое значение
    assert patched_data["lastname"] == sample_booking["lastname"]


def test_delete_booking(api, auth_token, sample_booking):
    """Тест: удаление бронирования (DELETE)"""
    created = api.create_booking(sample_booking)
    booking_id = created["bookingid"]

    # 1. Удаляем бронь
    delete_resp = api.delete_booking(booking_id, auth_token)
    assert delete_resp.status_code in [200, 201], f"Ожидался статус 200/201, получен {delete_resp.status_code}"

    # 2. Проверяем, что бронь больше не находится по ID (статус 404)
    get_resp = api.get_booking(booking_id)
    assert get_resp.status_code == 404, "Удаленная бронь не должна быть найдена"


def test_get_allbookingsids(api):
    """Тест: получение всех ID бронирований"""
    booking_ids = api.get_booking_ids()
    assert isinstance(booking_ids, list), "Ожидается список ID бронирований"
    assert len(booking_ids) > 0, "Список бронирований не должен быть пустым"
