import requests
import json

def test_api():
    # отправляем GET запрос для получения логина и пароля
    response = requests.get("https://test.ru/api/connect")
    # парсим ответ в формате JSON
    data = json.loads(response.text)
    # получаем логин и пароль
    login = data['eintires']['login']
    password = data['eintires']['password']
    # создаем тело POST запроса в формате JSON
    payload = {'login': login, 'password': password}
    # отправляем POST запрос с телом JSON
    response = requests.post("https://test.ru/api/v4/token", json=payload)
    # проверяем код ответа и выводим сообщение при неудаче
    if response.status_code != 200:
        print("Авторизация не удалась")