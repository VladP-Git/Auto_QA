import allure
import requests

@allure.epic("EPIC-123123")
class BookerApi:
    """Класс для работы с API сотрудников"""

    def __init__(self, url):
        """Инициализация с базовым URL"""
        self.url = url
    @allure.step('авторизация')
    def authenticate(self):
        credentials = {
            "username": "admin",
            "password": "password123"
        }
        with allure.step('отправка кредов'):
            resp = requests.post(f"{self.url}/auth", json=credentials)
            assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
            json_data = resp.json()
        with allure.step('проверка ответа'):
            assert "token" in json_data, "Ответ не содержит токен"
            assert json_data["token"], "Токен пустой"
            print(json_data["token"])
            return json_data["token"]

    def get_booking_ids(self):
        resp = requests.get(f"{self.url}/booking")
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        json_data = resp.json()
        assert all("bookingid" in item for item in json_data), "Ошибка: не все элементы содержат 'bookingid'"
        booking_ids = [item["bookingid"] for item in json_data]
        print(f"Получены ID бронирований: {booking_ids}")
        return booking_ids

    @allure.step("create new booking")
    def create_booking(self, booking):
        resp = requests.post(f"{self.url}/booking", json=booking)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def get_booking(self, booking_id):
        resp = requests.get(self.url + f'/booking/{booking_id}')
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def update_booking(self, booking_id, updated_data, token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": f"token={token}"
        }
        resp = requests.put(
            f"{self.url}/booking/{booking_id}",
            json=updated_data,
            headers=headers
        )
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def patch_booking(self, booking_id, patch_data, token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": f"token={token}"
        }
        resp = requests.patch(
            f"{self.url}/booking/{booking_id}",
            json=patch_data,
            headers=headers
        )
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def delete_booking(self, booking_id, token):
        headers = {
            "Cookie": f"token={token}"
        }
        resp = requests.delete(
            f"{self.url}/booking/{booking_id}",
            headers=headers
        )
        assert resp.status_code == 201, f"Ошибка: ожидался статус 201, получен {resp.status_code}"
        return True
