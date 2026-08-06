# Шпаргалка: HTTP, `requests`, `httpx` и API в Python

## 🌐 Клиент, сервер и API

```text
Клиент
→ отправляет запрос.

Сервер
→ принимает запрос и возвращает ответ.

HTTP
→ правила обмена данными между клиентом и сервером.

API
→ интерфейс для взаимодействия одной программы с другой.

Endpoint
→ адрес конкретной операции API.
```

Пример endpoint:

```text
https://httpbin.org/get
```

---

## 📡 Основные HTTP-методы

| Метод     | Назначение                          |
| --------- | ----------------------------------- |
| `GET`     | Получить данные                     |
| `POST`    | Создать ресурс или отправить данные |
| `PUT`     | Полностью заменить ресурс           |
| `PATCH`   | Частично изменить ресурс            |
| `DELETE`  | Удалить ресурс                      |
| `HEAD`    | Получить только заголовки           |
| `OPTIONS` | Узнать поддерживаемые методы        |

---

## 📦 Установка библиотек

```bash
poetry add requests httpx python-dotenv
```

Проверка:

```bash
poetry show requests
poetry show httpx
poetry show python-dotenv
```

---

## 🚀 Первый GET-запрос через `requests`

```python
import requests

url = "https://httpbin.org/get"

response = requests.get(url)

print(response)
```

Результат:

```text
<Response [200]>
```

Объект `Response` содержит информацию о запросе и ответе сервера.

---

## 📤 Структура HTTP-запроса

```text
Метод
URL
Параметры
Заголовки
Тело
```

Информация об отправленном запросе:

```python
print(response.request.method)
print(response.request.url)
print(response.request.headers)
print(response.request.body)
```

---

## 📥 Структура HTTP-ответа

```text
Статус-код
Описание статуса
Заголовки
Тело ответа
```

Основные свойства:

```python
print(response.status_code)
print(response.reason)
print(response.ok)
print(response.headers)
print(response.text)
```

Преобразование JSON в объекты Python:

```python
data = response.json()
```

```text
JSON-объект → dict
JSON-массив → list
JSON true   → True
JSON false  → False
JSON null   → None
```

---

## 🔢 Группы статус-кодов

| Группа | Значение               |
| ------ | ---------------------- |
| `1xx`  | Информационный ответ   |
| `2xx`  | Успешный запрос        |
| `3xx`  | Перенаправление        |
| `4xx`  | Ошибка запроса клиента |
| `5xx`  | Ошибка сервера         |

### Часто используемые статусы

```text
200 OK
→ запрос успешно выполнен.

201 Created
→ ресурс создан.

204 No Content
→ запрос выполнен, тело ответа отсутствует.

301 Moved Permanently
→ постоянное перенаправление.

302 Found
→ временное перенаправление.

400 Bad Request
→ неправильный запрос.

401 Unauthorized
→ отсутствует или неверен API-ключ или токен.

403 Forbidden
→ клиент определён, но операция запрещена.

404 Not Found
→ ресурс не найден.

422 Unprocessable Content
→ данные не прошли проверку.

429 Too Many Requests
→ превышен лимит запросов.

500 Internal Server Error
→ внутренняя ошибка сервера.

502 Bad Gateway
503 Service Unavailable
504 Gateway Timeout
→ проблемы на стороне сервиса или его инфраструктуры.
```

### Важно

```python
response.ok
```

возвращает `True` для статусов меньше `400`, поэтому `302` также считается `ok`.

Для проверки конкретного статуса:

```python
if response.status_code == 200:
    print("Получен успешный ответ")
```

---

## 🔍 GET-параметры

Параметры передаются через словарь:

```python
import requests

url = "https://httpbin.org/get"

params = {
    "city": "Moscow",
    "lang": "ru",
}

response = requests.get(
    url,
    params=params,
)

print(response.url)
print(response.json()["args"])
```

Итоговый URL:

```text
https://httpbin.org/get?city=Moscow&lang=ru
```

Не нужно собирать URL вручную: `requests` автоматически кодирует пробелы и специальные символы.

---

## 🧾 HTTP-заголовки

```python
headers = {
    "User-Agent": "weather-client/1.0",
    "Accept": "application/json",
}

response = requests.get(
    url,
    params=params,
    headers=headers,
)
```

Проверка отправленных заголовков:

```python
print(response.request.headers)
print(response.request.headers.get("User-Agent"))
```

```text
params
→ данные добавляются в URL.

headers
→ передают служебную информацию.
```

---

## 📮 POST и JSON-тело

```python
import requests

url = "https://httpbin.org/post"

data = {
    "city": "Moscow",
    "units": "metric",
}

response = requests.post(
    url,
    json=data,
)
```

Аргумент `json=`:

* преобразует словарь Python в JSON;
* помещает JSON в тело запроса;
* автоматически добавляет заголовок:

```text
Content-Type: application/json
```

Проверка:

```python
print(response.request.method)
print(response.request.headers.get("Content-Type"))
print(response.json()["json"])
```

---

## 🔄 Разница между `params`, `json` и `data`

```text
params=
→ параметры URL.

json=
→ JSON в теле запроса.

data=
→ данные формы или заранее подготовленное тело.
```

Для современных JSON API обычно используем:

```python
requests.post(url, json=data)
```

---

## ✏️ PUT-запрос

```python
updated_data = {
    "id": 1,
    "city": "Kazan",
    "units": "metric",
}

response = requests.put(
    "https://httpbin.org/put",
    json=updated_data,
)
```

```text
PUT
→ передаём полное новое состояние ресурса.

PATCH
→ передаём только изменяемые поля.
```

Общий вид PATCH:

```python
requests.patch(url, json=data)
```

---

## 🗑️ DELETE-запрос

```python
response = requests.delete(
    "https://httpbin.org/delete"
)

print(response.request.method)
print(response.request.body)
```

Обычно конкретный ресурс указывается в URL:

```text
DELETE /users/1
```

DELETE часто отправляется без тела запроса.

---

# 🌦️ Проект `weather-client`

## Структура

```text
weather-client/
├── examples/
│   └── http_practice.py
├── main.py
├── weather_api.py
├── weather_api_httpx.py
├── settings.py
├── .env
├── .env.example
├── .gitignore
├── pyproject.toml
└── poetry.lock
```

---

## 🔐 Хранение API-ключа

### `.env`

```dotenv
OPENWEATHER_API_KEY=ваш_настоящий_ключ
```

### `.env.example`

```dotenv
OPENWEATHER_API_KEY=
```

### `.gitignore`

```gitignore
.env
.venv/
__pycache__/
```

Настоящий API-ключ нельзя:

* записывать напрямую в Python-код;
* отправлять в Git;
* публиковать на GitHub;
* выводить вместе с полным URL запроса.

---

## ⚙️ Загрузка `.env`

Файл `settings.py`:

```python
import os

from dotenv import load_dotenv


load_dotenv()

OPENWEATHER_API_KEY = os.getenv(
    "OPENWEATHER_API_KEY"
)

if not OPENWEATHER_API_KEY:
    raise RuntimeError(
        "Не найден OPENWEATHER_API_KEY."
    )
```

```text
load_dotenv()
→ загружает значения из .env.

os.getenv()
→ получает переменную по имени.
```

---

# 📍 Geocoding API

Преобразует название города в координаты.

Endpoint:

```text
https://api.openweathermap.org/geo/1.0/direct
```

Параметры:

```python
params = {
    "q": city,
    "limit": 1,
    "appid": OPENWEATHER_API_KEY,
}
```

Запрос:

```python
response = requests.get(
    geocoding_url,
    params=params,
)
```

Ответ — список:

```python
locations = response.json()
location = locations[0]
```

Получение данных:

```python
coordinates = {
    "name": location["name"],
    "country": location["country"],
    "lat": location["lat"],
    "lon": location["lon"],
}
```

---

# 🌡️ Current Weather API

Получает текущую погоду по координатам.

Endpoint:

```text
https://api.openweathermap.org/data/2.5/weather
```

Параметры:

```python
params = {
    "lat": lat,
    "lon": lon,
    "appid": OPENWEATHER_API_KEY,
    "units": "metric",
    "lang": "ru",
}
```

```text
units=metric
→ температура в °C;
→ скорость ветра в м/с.

lang=ru
→ описание погоды на русском языке.
```

---

## Извлечение данных о погоде

```python
weather_data = response.json()

weather = {
    "city": weather_data["name"],
    "country": weather_data["sys"]["country"],
    "temperature": weather_data["main"]["temp"],
    "feels_like": weather_data["main"]["feels_like"],
    "humidity": weather_data["main"]["humidity"],
    "description": (
        weather_data["weather"][0]["description"]
    ),
    "wind_speed": weather_data["wind"]["speed"],
}
```

Не возвращаем весь ответ стороннего API — формируем собственный небольшой словарь.

---

# ⏱️ Таймауты

```python
response = requests.get(
    url,
    params=params,
    timeout=10,
)
```

Таймаут ограничивает ожидание сетевой операции.

У `requests` таймаут нужно указывать явно.

---

## ❗ Проверка HTTP-статуса

```python
response.raise_for_status()
```

Метод создаёт `HTTPError`, если сервер вернул `4xx` или `5xx`.

Правильный порядок:

```python
response = requests.get(
    url,
    params=params,
    timeout=10,
)

response.raise_for_status()

data = response.json()
```

---

# 🛡️ Исключения `requests`

```python
try:
    response = requests.get(
        url,
        params=params,
        timeout=10,
    )

    response.raise_for_status()

    data = response.json()

except requests.exceptions.Timeout:
    print("Сервер не ответил вовремя")

except requests.exceptions.ConnectionError:
    print("Не удалось подключиться")

except requests.exceptions.HTTPError:
    print("Получена HTTP-ошибка")

except requests.exceptions.JSONDecodeError:
    print("Ответ не является корректным JSON")

except requests.exceptions.RequestException:
    print("Другая ошибка requests")
```

Не используем без необходимости:

```python
except Exception:
```

Конкретные исключения помогают понять причину ошибки.

---

## 🧩 Ошибки структуры данных

```python
if not locations:
    raise WeatherAPIError(
        f"Город '{city}' не найден."
    )
```

```python
try:
    latitude = location["lat"]
    longitude = location["lon"]

except (KeyError, IndexError, TypeError):
    raise WeatherAPIError(
        "API вернул неполные данные."
    )
```

---

# 🖥️ Консольное приложение

Основной сценарий:

```python
city = input(
    "Введите название города: "
).strip()

if not city:
    print(
        "Название города не может быть пустым."
    )
    return

coordinates = get_coordinates(city)

weather = get_weather(
    coordinates["lat"],
    coordinates["lon"],
)
```

Вывод:

```python
print(
    f"Город: {weather['city']}, "
    f"{weather['country']}"
)

print(
    f"Температура: "
    f"{weather['temperature']} °C"
)

print(
    f"Ощущается как: "
    f"{weather['feels_like']} °C"
)

print(
    f"Погода: {weather['description']}"
)

print(
    f"Влажность: {weather['humidity']} %"
)

print(
    f"Скорость ветра: "
    f"{weather['wind_speed']} м/с"
)
```

---

# ⚡ Переход с `requests` на `httpx`

## Синхронный запрос

### `requests`

```python
response = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=10,
)
```

### `httpx`

```python
response = httpx.get(
    url,
    params=params,
    headers=headers,
    timeout=10.0,
)
```

Основной синхронный интерфейс почти одинаковый.

---

## Сравнение исключений

| `requests`                             | `httpx`                  |
| -------------------------------------- | ------------------------ |
| `requests.exceptions.Timeout`          | `httpx.TimeoutException` |
| `requests.exceptions.ConnectionError`  | `httpx.RequestError`     |
| `requests.exceptions.HTTPError`        | `httpx.HTTPStatusError`  |
| `requests.exceptions.RequestException` | `httpx.RequestError`     |
| `requests.exceptions.JSONDecodeError`  | `json.JSONDecodeError`   |

---

## Обработка ошибок HTTPX

```python
import json

import httpx


try:
    response = httpx.get(
        url,
        params=params,
        timeout=10.0,
    )

    response.raise_for_status()

    data = response.json()

except httpx.TimeoutException:
    print("Сервер не ответил вовремя")

except httpx.HTTPStatusError:
    print("Получена HTTP-ошибка")

except json.JSONDecodeError:
    print("Некорректный JSON")

except httpx.RequestError:
    print("Ошибка выполнения запроса")
```

---

## 🔄 `requests` и `httpx`

| Возможность                 | `requests` | `httpx`       |
| --------------------------- | ---------- | ------------- |
| Синхронные запросы          | Да         | Да            |
| Асинхронные запросы         | Нет        | Да            |
| `params`, `headers`, `json` | Да         | Да            |
| `raise_for_status()`        | Да         | Да            |
| Таймаут по умолчанию        | Нет        | Есть          |
| Клиент с соединениями       | `Session`  | `Client`      |
| Асинхронный клиент          | Нет        | `AsyncClient` |

---

## Асинхронный HTTPX — только внешний вид

```python
async def load_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://example.com/api"
        )

        response.raise_for_status()

        return response.json()
```

Для работы такого кода необходимо изучить:

```text
async
await
asyncio
цикл событий
```

В рамках текущего занятия асинхронный подход подробно не разбирается.

---

# ✅ Итоговый сценарий проекта

```text
Пользователь вводит город
        ↓
get_coordinates()
        ↓
Geocoding API
        ↓
lat и lon
        ↓
get_weather()
        ↓
Current Weather API
        ↓
подготовленный словарь
        ↓
вывод результата
```

---

## ⚠️ Важные моменты

* URL с параметрами лучше не собирать вручную.
* Для GET-параметров используйте `params=`.
* Для JSON-тела используйте `json=`.
* Всегда задавайте таймаут для `requests`.
* После запроса вызывайте `raise_for_status()`.
* Проверяйте структуру JSON перед использованием.
* Не храните API-ключ в исходном коде.
* Не добавляйте `.env` в Git.
* Не выводите URL, содержащий API-ключ.
* Обрабатывайте конкретные исключения.
* Не передавайте наружу весь ответ стороннего API.
* Синхронный интерфейс `httpx` похож на `requests`.
