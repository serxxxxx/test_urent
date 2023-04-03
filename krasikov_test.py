import requests
import json

def test_api():
    # ���������� GET ������ ��� ��������� ������ � ������
    response = requests.get("https://test.ru/api/connect")
    # ������ ����� � ������� JSON
    data = json.loads(response.text)
    # �������� ����� � ������
    login = data['eintires']['login']
    password = data['eintires']['password']
    # ������� ���� POST ������� � ������� JSON
    payload = {'login': login, 'password': password}
    # ���������� POST ������ � ����� JSON
    response = requests.post("https://test.ru/api/v4/token", json=payload)
    # ��������� ��� ������ � ������� ��������� ��� �������
    if response.status_code != 200:
        print("����������� �� �������")