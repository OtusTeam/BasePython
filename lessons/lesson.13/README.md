## Установка виртуального окружения 
python -m venv ./.myvenv  
source ./.venv/bin/activate  
./.venv/Scripts/activate  
./.venv/Scripts/activate.ps1  
  

# Занятие 13. Тестирование Python-кода с pytest

## 1. Что такое pytest и зачем он нужен

**pytest** — это фреймворк для автоматического тестирования Python-кода.

Он позволяет:
- автоматически проверять корректность работы функций и модулей;
- находить ошибки сразу после изменений в коде;
- безопасно рефакторить код;
- документировать ожидаемое поведение программы через тесты.

Ключевая идея pytest:
> тест — это обычная функция Python + `assert`

---

## 2. Установка и базовые команды

### Установка
```bash
pip install pytest pytest-cov pytest-mock
```

### Проверка установки
```bash
pytest --version
```

### Запуск всех тестов
```bash
pytest
pytest -v        # подробный вывод
pytest -vv       # максимально подробный вывод
```

### Запуск конкретного файла
```bash
pytest tests/test_calc.py
```

### Запуск одного теста
```bash
pytest tests/test_calc.py::test_add
```

---

## 3. Как pytest находит тесты

pytest автоматически ищет:

- файлы:
  - `test_*.py`
  - `*_test.py`
- функции:
  - `def test_*():`
- классы:
  - `class Test*:`

Никаких регистраций тестов делать не нужно.

---

## 4. Простейший тест

```python
def test_add():
    result = add(2, 3)
    assert result == 5
```

Если `assert` ложный — тест падает.  
Если истинный — тест считается успешным.

---

## 5. Проверка исключений

Если функция **обязана выбрасывать ошибку**, это нужно тестировать явно.

```python
import pytest

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(10, 0)
```

Можно также проверять текст ошибки:

```python
with pytest.raises(ValueError, match="Деление"):
    div(10, 0)
```

---

## 6. Параметризация (`@pytest.mark.parametrize`)

Позволяет запускать **один и тот же тест с разными данными**.

```python
import pytest

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (5, 5, 10),
        (-1, -2, -3),
    ]
)
def test_add_param(a, b, expected):
    assert add(a, b) == expected
```

Что происходит:
- pytest создаёт **несколько тестов** из одного
- каждый набор данных — отдельный прогон

---

## 7. Фикстуры (`@pytest.fixture`)

Фикстуры используются для:
- подготовки данных;
- подготовки окружения;
- устранения дублирования кода.

### Простая фикстура

```python
import pytest

@pytest.fixture
def numbers():
    return 10, 5

def test_sub(numbers):
    a, b = numbers
    assert sub(a, b) == 5
```

pytest сам:
- вызывает фикстуру;
- передаёт её результат в тест по имени.

---

## 8. scope фикстур

`scope` определяет, **как долго живёт фикстура**.

| scope      | Когда создаётся | Когда уничтожается |
|-----------|----------------|-------------------|
| function  | перед каждым тестом | после каждого теста |
| class     | один раз на класс | после класса |
| module    | один раз на файл | после файла |
| session   | один раз на все тесты | после pytest |

Пример:

```python
@pytest.fixture(scope="module")
def resource():
    return {"status": "ok"}
```

---

## 9. yield в фикстурах (setup / teardown)

`yield` позволяет освободить ресурсы после теста.

```python
@pytest.fixture
def resource():
    print("setup")
    yield {"status": "ready"}
    print("teardown")
```

Код:
- **до `yield`** — выполняется перед тестом
- **после `yield`** — после завершения теста

---

## 10. conftest.py

`conftest.py` — файл с **общими фикстурами**, доступными без импорта.

Структура:
```
tests/
├── conftest.py
├── test_calc.py
```

Пример:

```python
# tests/conftest.py
import pytest

@pytest.fixture
def base_numbers():
    return 3, 7
```

Теперь `base_numbers` доступна во всех тестах проекта.

---

## 11. Моки и подмена зависимостей (`pytest-mock`)

Моки нужны, чтобы:
- изолировать код;
- убрать случайность;
- не ходить в реальные API;
- ускорить тесты.

Пример:

```python
def test_random(mocker):
    mocker.patch("random.randint", return_value=42)
    import random
    assert random.randint(1, 100) == 42
```

`mocker.patch()` временно подменяет функцию.

---

## 12. Тестирование print и вывода в консоль (`capsys`)

`capsys` перехватывает:
- `stdout` (print)
- `stderr` (ошибки)

```python
def test_print(capsys):
    print("Hello")
    captured = capsys.readouterr()
    assert captured.out == "Hello\n"
```

Поля:
- `captured.out` — stdout
- `captured.err` — stderr

---

## 13. Покрытие кода (`pytest-cov`)

Покрытие показывает, **какие строки кода реально выполнялись**.

### Запуск с покрытием
```bash
pytest --cov=src
```

### Показать непокрытые строки
```bash
pytest --cov=src --cov-report=term-missing
```

### HTML-отчёт
```bash
pytest --cov=src --cov-report=html
```

Файл отчёта:
```
htmlcov/index.html
```

---

## 14. Полезные флаги pytest

| Флаг | Назначение |
|-----|-----------|
| `-v` | подробный вывод |
| `-x` | остановка на первой ошибке |
| `--lf` | запустить только упавшие тесты |
| `-s` | показать print |
| `--maxfail=1` | максимум ошибок |
| `--cov-fail-under=80` | минимальное покрытие |

---

## 15. Как мыслить при написании тестов

✔ проверяем **поведение**, а не реализацию  
✔ один тест — одна логическая проверка  
✔ тест должен быть читаемым без комментариев  
✔ фикстуры вместо копипаста  
✔ моки — только там, где без них нельзя  

---
