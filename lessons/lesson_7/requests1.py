import requests

def test_simple_req():
    resp = requests.get('http://5.101.50.27:8000/company/list')
    assert resp.status_code == 200  # Проверяем, что сервер вернул статус 200 (OK)


def test_simple_req_2():
    resp = requests.get('http://5.101.50.27:8000/company/list')

    assert resp.status_code == 200  # Проверяем успешный статус
    assert resp.headers["Content-Type"] == "application/json"  # Проверяем тип контента

def test_simple_req_3():
    resp = requests.get('https://restful-booker.herokuapp.com/booking')

    response_body = resp.json()  # Преобразуем ответ в Dict
    first_company = response_body[0]  # Получаем первую компанию из списка

    assert first_company["name"] == "QA Студия 'ТестировщикЪ'"
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"


