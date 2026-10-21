import pytest
import requests

from booker_api import BookerApi
import allure

base_url = "https://restful-booker.herokuapp.com"
api = BookerApi(base_url)

@allure.id("SAUCEDEMO-17")
@allure.title("авторизация")
@allure.severity(allure.severity_level.BLOCKER)
def test_authentication():
    api.authenticate()

@allure.id("WIKIPEDIA-4")
@allure.title("получение всех броней 2")
@pytest.mark.skip(reason="Skipping for demo")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_booking_ids():
    api.get_booking_ids()

@allure.id("ITCH-3")
@allure.title("создание брони")
@allure.severity(allure.severity_level.MINOR)
def test_create_booking():
    booking = {
        "firstname": "Roman",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    resp = api.create_booking(booking)
    assert resp["bookingid"] != "", "Нет id"

def test_get_booking():
    with allure.step("step one — generate test data"):
        booking = {
            "firstname": "Rom",
            "lastname": "White",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }

    new_booking = api.create_booking(booking)
    booking_id = new_booking["bookingid"]

    with allure.step(f"step three — verify booking with {booking_id}"):
        resp = api.get_booking(booking_id)
        assert resp["firstname"] == "Rom"

def test_update_booking():
    # Step 1: Authenticate and get token
    token = api.authenticate()

    # Step 2: Create a booking
    with allure.step("step one — generate test data"):
        booking = {
            "firstname": "Tom",
            "lastname": "Smith",
            "totalprice": 150,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2023-01-01",
                "checkout": "2023-01-10"
            },
            "additionalneeds": "Dinner"
        }

    new_booking = api.create_booking(booking)
    booking_id = new_booking["bookingid"]

    # Step 3: Prepare update data
    updated_booking = {
        "firstname": "Tommy",
        "lastname": "Smith",
        "totalprice": 200,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2023-01-02",
            "checkout": "2023-01-12"
        },
        "additionalneeds": "Lunch"
    }

    # Step 4: Perform update
    updated_resp = api.update_booking(booking_id, updated_booking, token)

    # Step 5: Validate response
    assert updated_resp["firstname"] == "Tommy", "Имя не обновилось"
    assert updated_resp["totalprice"] == 200, "Цена не обновилась"
    assert updated_resp["depositpaid"] is False, "Статус депозита не обновился"

@allure.description("Привет, ITCH!")
def test_patch_booking():
    # Step 1: Authenticate and get token
    token = api.authenticate()

    # Step 2: Create a full booking
    booking = {
        "firstname": "Anna",
        "lastname": "Taylor",
        "totalprice": 300,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-05-01",
            "checkout": "2023-05-10"
        },
        "additionalneeds": "Dinner"
    }
    new_booking = api.create_booking(booking)
    booking_id = new_booking["bookingid"]

    # Step 3: Prepare partial update data
    patch_data = {
        "firstname": "Anastasia",
        "lastname": "Ivanova"
    }

    # Step 4: Perform PATCH
    patched_resp = api.patch_booking(booking_id, patch_data, token)

    # Step 5: Validate partial update
    assert patched_resp["firstname"] == "Anastasia", "Имя не обновилось"
    assert patched_resp["lastname"] == "Ivanova", "Фамилия не обновилась"
    assert patched_resp["totalprice"] == 300, "Цена не должна была измениться"

@allure.feature("POL-168/POL-169/POL-170")
def test_delete_booking():
    # Step 1: Authenticate and get token
    token = api.authenticate()

    # Step 2: Create a booking to delete
    booking = {
        "firstname": "DeleteMe",
        "lastname": "Now",
        "totalprice": 123,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2022-10-01",
            "checkout": "2022-10-05"
        },
        "additionalneeds": "None"
    }
    new_booking = api.create_booking(booking)
    booking_id = new_booking["bookingid"]

    # Step 3: Delete the booking
    result = api.delete_booking(booking_id, token)
    assert result is True, "Удаление не удалось"

    # Step 4: Try to get the deleted booking (should 404)
    resp = requests.get(f"{api.url}/booking/{booking_id}")
    assert resp.status_code == 404, "Бронирование не удалено (ожидался 404)"
