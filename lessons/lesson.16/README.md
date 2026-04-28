# Шпаргалка: Работа с HTTP и API

## 🌐 requests - HTTP запросы

### Основные методы:
- `get()` - GET запрос
- `post()` - POST запрос  
- `put()` - PUT запрос
- `delete()` - DELETE запрос

```python
import requests

# GET запрос
response = requests.get('https://api.example.com/data')
response = requests.get('https://api.example.com/data', params={'key': 'value'})

# POST запрос
response = requests.post('https://api.example.com/data', json={'name': 'Alice'})
response = requests.post('https://api.example.com/data', data={'name': 'Alice'})

# Заголовки
headers = {'User-Agent': 'My App', 'Authorization': 'Bearer token'}
response = requests.get(url, headers=headers)
```

### Работа с ответом:
```python
response = requests.get('https://api.example.com/data')

# Статус код
print(response.status_code)  # 200, 404, 500...

# Содержимое
print(response.text)         # Текст
print(response.json())       # JSON как словарь
print(response.content)      # Байты

# Заголовки
print(response.headers)
```

---

## 📊 Работа с JSON

### Основные операции:
```python
import json

# Преобразование в JSON
data = {'name': 'Alice', 'age': 30}
json_string = json.dumps(data)

# Преобразование из JSON  
json_string = '{"name": "Alice", "age": 30}'
data = json.loads(json_string)

# Работа с файлами
with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    data = json.load(f)
```

---

## 🔑 Работа с API

### Получение данных:
```python
# Погода (OpenWeatherMap)
api_key = "your_api_key"
city = "Moscow"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
if response.status_code == 200:
    weather = response.json()
    temp = weather['main']['temp']
    print(f"Температура: {temp}K")
```

### Обработка ошибок:
```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Вызвать исключение для HTTP ошибок
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")
except requests.exceptions.Timeout:
    print("Превышено время ожидания")
except json.JSONDecodeError:
    print("Ошибка парсинга JSON")
```

---

## 📡 Популярные бесплатные API

### Примеры запросов:

**Random Cat API:**
```python
response = requests.get('https://api.thecatapi.com/v1/images/search')
cat_url = response.json()[0]['url']
```

**Numbers API:**
```python
number = 42
response = requests.get(f'http://numbersapi.com/{number}')
fact = response.text
```

**JSONPlaceholder (тестовый API):**
```python
# Получить пост
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Создать пост
new_post = {'title': 'My Title', 'body': 'My content', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)
```

---

## 🛠️ Полезные паттерны

### Сохранение изображения:
```python
response = requests.get('https://example.com/image.jpg')
if response.status_code == 200:
    with open('image.jpg', 'wb') as f:
        f.write(response.content)
```

### Работа с сессиями:
```python
session = requests.Session()
session.headers.update({'User-Agent': 'My App'})

response1 = session.get('https://api.example.com/login')
response2 = session.get('https://api.example.com/data')  # Cookies сохранены
```

### Интерактивное меню для выбора API:
```python
def choose_api():
    print("1. Погода")
    print("2. Случайный кот")
    print("3. Факт о числе")
    
    choice = input("Выберите опцию: ")
    
    if choice == '1':
        return get_weather()
    elif choice == '2':
        return get_random_cat()
    elif choice == '3':
        return get_number_fact()
```

---

## ⚠️ Важные моменты

- Всегда проверяйте `status_code`
- Используйте `timeout` для избежания зависания
- Не забывайте про API ключи и лимиты
- Обрабатывайте исключения
- Уважайте ограничения API (rate limits) 