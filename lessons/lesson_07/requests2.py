import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(resp.text)  # Получаем ответ в виде строки
print(type(resp.text))
data = resp.json()  # Преобразуем JSON в Python-объект
print(data["title"])  # Теперь можно обращаться к данным как к словарю