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


def test_filter_booking_by_name(api,sample_booking):
    booking_data = sample_booking.copy()
    booking_data["firstname"] = 'testfirstname'
    booking_data["lastname"] = 'testlastname'
    created = api.create_booking(booking_data)
    booking_id = created["bookingid"]
    params = {
        "firstname": 'testfirstname',
        "lastname": 'testlastname'
    }
    boking_ids = api.get_booking_ids(params)
    found_ids = [item["bookingid"] for item in boking_ids]
    assert booking_id in found_ids


def test_get_nonexistent_booking(api):
    """Тест 2: получение несуществующего бронирования"""

    # Отправляем GET-запрос на получение списка бронирований.
    # Без параметров фильтрации API возвращает список доступных ID.
    booking_ids = api.get_booking_ids()

    # Из списка словарей извлекаем все ID в отдельный список.
    # Пример результата: [1, 2, 3, 4].
    existing_ids = [item["bookingid"] for item in booking_ids]

    # Выбираем ID, который значительно превышает максимальный
    # ID из полученного списка.
    #
    # max(existing_ids) возвращает наибольший ID.
    # Если список пустой, default=0 позволит использовать 0.
    # Прибавляем 100000, чтобы выбрать ID за пределами текущего диапазона.
    nonexistent_id = max(existing_ids, default=0) + 13

    # Отправляем GET-запрос на получение бронирования по выбранному ID.
    # Ответ сохраняем в resp, чтобы проверить HTTP-статус.
    resp = api.get_booking(nonexistent_id)

    # Ожидаем HTTP 404 Not Found — бронирование не найдено.
    # Если сервер вернёт другой статус, тест завершится ошибкой.
    assert resp.status_code == 404, (
        f"Ожидался статус 404, получен {resp.status_code}"
    )




    def test_create_pruf(api, sample_booking):
        """Тест: создание бронирования с проверкой структуры ответа"""
        created_booking = api.create_booking(sample_booking)
        keys_std = ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates", "additionalneeds"]
        keys = list(created_booking['booking'].keys())
        print(keys)
        for key in keys_std:
            assert key in keys, f"Ключ {key} отсутствует в ответе API"






