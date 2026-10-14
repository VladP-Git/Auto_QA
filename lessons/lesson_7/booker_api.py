import requests

class BookerApi:
    """Класс для взаимодействия с API Restful-Booker"""

    def __init__(self, base_url="https://restful-booker.herokuapp.com"):
        self.base_url = base_url

    def get_auth_token(self, username="admin", password="password123"):
        """Получение токена авторизации"""
        payload = {"username": username, "password": password}
        resp = requests.post(f"{self.base_url}/auth", json=payload)
        assert resp.status_code == 200, f"Ошибка авторизации: {resp.status_code}"
        return resp.json()["token"]

    def get_booking_ids(self, params=None):
        """Получить список всех ID бронирований (с фильтрацией или без)"""
        resp = requests.get(f"{self.base_url}/booking", params=params)
        assert resp.status_code == 200, f"Ошибка получения списка: {resp.status_code}"
        return resp.json()

    def get_booking(self, booking_id):
        """Получить детали бронирования по ID"""
        resp = requests.get(f"{self.base_url}/booking/{booking_id}")
        return resp

    def create_booking(self, booking_data):
        """Создать новое бронирование"""
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        resp = requests.post(f"{self.base_url}/booking", json=booking_data, headers=headers)
        assert resp.status_code == 200, f"Ошибка создания: {resp.status_code} - {resp.text}"
        return resp.json()

    def update_booking(self, booking_id, booking_data, token):
        """Полное обновление бронирования (PUT)"""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": f"token={token}"
        }
        resp = requests.put(f"{self.base_url}/booking/{booking_id}", json=booking_data, headers=headers)
        return resp

    def partial_update_booking(self, booking_id, update_data, token):
        """Частичное обновление бронирования (PATCH)"""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": f"token={token}"
        }
        resp = requests.patch(f"{self.base_url}/booking/{booking_id}", json=update_data, headers=headers)
        return resp

    def delete_booking(self, booking_id, token):
        """Удаление бронирования (DELETE)"""
        headers = {
            "Content-Type": "application/json",
            "Cookie": f"token={token}"
        }
        resp = requests.delete(f"{self.base_url}/booking/{booking_id}", headers=headers)
        return resp
