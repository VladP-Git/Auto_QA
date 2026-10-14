import json  # Подключаем модуль json

company_json = """
{
    "id": 111,
    "isActive": true,
    "createDateTime": "2024-04-05T17:30:00.713Z",
    "lastChangedDateTime": "2024-04-05T17:30:00.713Z",
    "name": "Барбершоп 'Цирюльникъ'",  
    "description": "Крутые стрижки для крутых шишек"
}
"""

def test_parse_json():
    print(company_json)
    company = json.loads(company_json)  # Преобразуем JSON в словарь
    print(company)
    assert company["id"] == 111  # Проверяем значение ключа "id"

company_list_json = """
[
    {
        "id": 111,
        "isActive": true,
        "createDateTime": "2024-04-05T17:30:00.713Z",
        "lastChangedDateTime": "2024-04-05T17:30:00.713Z",
        "name": "Барбершоп 'Цирюльникъ'",
        "description": "Крутые стрижки для крутых шишек"
    },
    {
        "id": 112,
        "isActive": true,
        "createDateTime": "2024-04-05T17:30:00.713Z",
        "lastChangedDateTime": "2024-04-05T17:30:00.713Z",
        "name": "Кондитерская Профи-троли",
        "description": "Сладко и точка"
    },
    {
        "id": 113,
        "isActive": true,
        "createDateTime": "2024-04-05T17:30:00.713Z",
        "lastChangedDateTime": "2024-04-05T17:30:00.713Z",
        "name": "Муж на час",
        "description": "Помощь в делах"
    }
]
"""

def test_parse_array_json():
    company_list = json.loads(company_list_json)  # Преобразуем JSON в список словарей
    assert len(company_list) == 3  # Проверяем длину списка


def test_parse_array_json2():
    company_list = json.loads(company_list_json)

    first_company = company_list[0]  # Первая компания (индекс 0)
    assert first_company["name"] == "Барбершоп 'Цирюльникъ'"  # Проверяем название компании

    # Проверяем ID второй компании
    assert company_list[1]["id"] == 112
