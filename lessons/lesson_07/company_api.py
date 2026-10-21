import requests

class CompanyApi:
    """Класс для взаимодействия с API компаний"""

    def __init__(self, url):
        """Инициализация класса с базовым URL API"""
        self.url = url
    def get_company_list(self):
        """Получить список всех компаний"""
        resp = requests.get(self.url + '/company/list')
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()
    def get_token(self, user, password):
        """Получить токен авторизации"""
        creds = {"username": user, "password": password}
        resp = requests.post(self.url + '/auth/login', json=creds)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()["user_token"]
    def create_company(self, name, description=""):
        """Создать новую компанию"""
        company = {"name": name, "description": description}
        resp = requests.post(self.url + '/company/create', json=company)
        assert resp.status_code == 201, f"Ошибка: ожидался статус 201, получен {resp.status_code}"
        return resp.json()
    def get_company(self, company_id):
        """Получить информацию о компании по ID"""
        resp = requests.get(self.url + f'/company/{company_id}')
        # assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()
    def edit_company(self, company_id, new_name, new_descr, user, password):
        """Изменить название и описание компании по ID"""
        client_token = self.get_token(user, password)
        url_with_token = f"{self.url}/company/update/{company_id}?client_token={client_token}"

        company_data = {
            "name": new_name,
            "description": new_descr
        }
        resp = requests.patch(url_with_token, json=company_data)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def delete_company(self, company_id, user, password):
        """Удалить компанию по ID"""
        client_token = self.get_token(user, password)
        url_with_token = f"{self.url}/company/{company_id}?client_token={client_token}"

        resp = requests.delete(url_with_token)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()
    def set_active_state(self, company_id, is_active, user, password):
        """Изменить статус активности компании"""
        client_token = self.get_token(user, password)
        url_with_token = f"{self.url}/company/status_update/{company_id}?client_token={client_token}"
        resp = requests.patch(url_with_token, json={"is_active": is_active})
        assert resp.status_code == 202, f"Ошибка: ожидался статус 202, получен {resp.status_code}"
        return resp.json()

