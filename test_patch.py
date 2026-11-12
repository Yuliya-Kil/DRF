import requests

url = "http://127.0.0.1:8000/api/advertisements/1/"

headers = {
    "Authorization": "Token 96a71e2dc4a33d641c274ce8c203231c84861a23",
    "Content-Type": "application/json"
}

body = {
    "title": "Шкаф в цвете дуб крафт золотой"
}

response = requests.patch(url, json=body, headers=headers)

print(f"Статус: {response.status_code}")
print(response.text)

