# Шпаргалка: Встроенные модули Python

## 📋 argparse - Парсинг аргументов командной строки

### Основные функции:
- `ArgumentParser()` - создать парсер аргументов
- `add_argument()` - добавить аргумент
- `parse_args()` - разобрать аргументы

```python
import argparse

parser = argparse.ArgumentParser(description='Описание программы')
parser.add_argument('name', help='Позиционный аргумент')
parser.add_argument('-v', '--verbose', action='store_true', help='Подробный вывод')
parser.add_argument('-f', '--file', default='input.txt', help='Файл для обработки')
args = parser.parse_args()
```

---

## 🔍 logging - Логирование

### Основные функции:
- `basicConfig()` - базовая настройка логирования
- `debug()`, `info()`, `warning()`, `error()`, `critical()` - уровни логирования
- `getLogger()` - получить логгер

```python
import logging

# Настройка
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Использование
logging.info('Информационное сообщение')
logging.warning('Предупреждение')
logging.error('Ошибка')

# Логирование в файл
logging.basicConfig(filename='app.log', level=logging.DEBUG)
```

---

## 🔤 re - Регулярные выражения

### Основные функции:
- `search()` - найти первое совпадение
- `match()` - проверить совпадение с начала строки
- `findall()` - найти все совпадения
- `sub()` - заменить совпадения
- `split()` - разделить строку

```python
import re

# Поиск
result = re.search(r'\d+', 'abc123def')  # Найти число
matches = re.findall(r'\w+@\w+\.\w+', text)  # Найти email

# Замена
new_text = re.sub(r'\d+', 'NUMBER', 'abc123def')  # Заменить числа

# Разделение
parts = re.split(r'[,;]', 'apple,banana;orange')  # Разделить по запятой или точке с запятой
```

### Основные паттерны:
- `\d` - цифра
- `\w` - буква/цифра/подчеркивание  
- `\s` - пробел
- `+` - один или более
- `*` - ноль или более
- `?` - ноль или один

---

## 🗂️ collections - Специальные коллекции

### Counter - подсчет элементов
```python
from collections import Counter

# Подсчет элементов
counter = Counter(['apple', 'banana', 'apple', 'cherry'])
print(counter.most_common(2))  # [('apple', 2), ('banana', 1)]
```

### defaultdict - словарь с значением по умолчанию
```python
from collections import defaultdict

dd = defaultdict(list)
dd['key'].append('value')  # Не вызывает KeyError
```

### deque - двусторонняя очередь
```python
from collections import deque

d = deque(['a', 'b', 'c'])
d.appendleft('z')  # Добавить слева
d.pop()           # Удалить справа
```

### namedtuple - именованный кортеж
```python
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])
p = Person('Alice', 30, 'Moscow')
print(p.name)  # Alice
```

---

## 🎯 Практические примеры

### CLI утилита с аргументами и логированием:
```python
import argparse
import logging

parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true')
args = parser.parse_args()

level = logging.DEBUG if args.debug else logging.INFO
logging.basicConfig(level=level)
```

### Анализ текста с regex и Counter:
```python
import re
from collections import Counter

text = "Hello world! Hello Python!"
words = re.findall(r'\w+', text.lower())
word_count = Counter(words)
print(word_count.most_common())
``` 