import requests

url = "http://127.0.0.1:8000/api/advertisements/"

print("=== Тест для гостя (ожидаем 429 на 11-м) ===")
for i in range(1, 13):
    resp = requests.get(url)
    print(f"Запрос {i}: {resp.status_code}")

token = "96a71e2dc4a33d641c274ce8c203231c84861a23"  # <-- подставь настоящий токен, формат: Token <ключ>

print("=== Тест для авторизованного (ожидаем 429 на 21-м) ===")
for i in range(1, 23):
    resp = requests.get(url, headers={"Authorization": f"Token {token}"})
    print(f"Запрос {i}: {resp.status_code}
")
