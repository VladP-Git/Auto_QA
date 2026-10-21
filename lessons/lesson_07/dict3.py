import json

invalid_json = "{ 'id': 111, 'name': 'Test Company' }"  # Неправильные одинарные кавычки
company_json = """
{
    "id": 111,
    "isActive": True,
    "createDateTime": null,
    "lastChangedDateTime": "2024-04-05T17:30:00.713Z",
    "name": "Барбершоп 'Цирюльникъ'",
    "description": "Крутые стрижки для крутых шишек"
}
"""

def test_parse_json():
    invalid_json = json.loads(company_json)
    print(invalid_json)

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"Ошибка при разборе JSON: {e}")
