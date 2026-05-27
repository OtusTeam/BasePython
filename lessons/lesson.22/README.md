# pip, venv и Poetry

---

## 1. PyPI

PyPI - это основной каталог Python-библиотек.

Пример страницы пакета Django:

```text
https://pypi.org/project/Django/
````

На PyPI можно смотреть:

* название пакета;
* актуальную версию;
* команду для установки;
* описание библиотеки;
* зависимости;
* документацию и ссылки на проект.

---

## 2. Виртуальное окружение

Виртуальное окружение нужно, чтобы зависимости одного проекта не мешали другим проектам.

### Создать виртуальное окружение

```bash
python3 -m venv ./myvenv
```

### Активировать на Linux / macOS

```bash
source ./myvenv/bin/activate
```

### Активировать на Windows CMD

```bash
./myvenv/Scripts/activate
```

### Активировать на Windows PowerShell

```powershell
./myvenv/Scripts/Activate.ps1
```


### Выйти из виртуального окружения

```bash
deactivate
```

---

## 3. pip

`pip` - стандартный менеджер пакетов Python.

### Проверить версию pip

```bash
pip --version
```

### Посмотреть установленные пакеты

```bash
pip list
```

### Установить пакет

```bash
pip install requests
```

### Установить конкретную версию

```bash
pip install requests==2.26
```

### Обновить пакет

```bash
pip install --upgrade requests
```

### Удалить пакет

```bash
pip uninstall requests
```

---

## 4. requirements.txt

Файл `requirements.txt` хранит список зависимостей проекта.

### Сохранить текущие зависимости

```bash
pip freeze > requirements.txt
```

### Установить зависимости из файла

```bash
pip install -r requirements.txt
```

Обычно этот файл добавляют в проект, чтобы другой разработчик мог быстро установить те же зависимости.

---

## 5. Установка Poetry

Poetry - инструмент для управления зависимостями, виртуальным окружением и 
настройками проекта.

Документация:

```text
https://python-poetry.org/docs/#installing-with-the-official-installer
```

### Linux, macOS, Windows WSL

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Windows PowerShell

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

### Проверить версию Poetry

```bash
poetry --version
```

---

## 6. Создание проекта в Poetry

### Создать новый проект

```bash
poetry new my_project
```

Poetry создаст папку проекта со стандартной структурой.

### Инициализировать Poetry в существующем проекте

```bash
poetry init
```

Команда создаёт файл `pyproject.toml`.

---

## 7. Установка зависимостей через Poetry

### Добавить обычную зависимость

```bash
poetry add requests
```

```bash
poetry add fastapi
```


### Добавить зависимость в группу dev

```bash
poetry add pytest --group dev
```

Группа `dev` обычно используется для инструментов разработки и тестирования.

### Добавить зависимость в группу lint

```bash
poetry add black --group lint
```

Группа `lint` обычно используется для форматтеров и линтеров.

---

## 8. Удаление зависимостей

### Удалить пакет

```bash
poetry remove requests
```

Если пакет был в группе, Poetry сам удалит его из нужного места.

---

## 9. Информация об окружении

### Посмотреть информацию о виртуальном окружении

```bash
poetry env info
```

Команда показывает путь к окружению, версию Python и другую информацию.

---

## 10. Обновление зависимостей

### Обновить все зависимости

```bash
poetry update
```

### Обновить конкретный пакет

```bash
poetry update requests
```

---

## 11. Проверка проекта

### Проверить настройки Poetry

```bash
poetry check
```

Команда проверяет корректность `pyproject.toml`.

### Посмотреть настройки Poetry

```bash
poetry config --list
```

---

## 12. Установка зависимостей по группам

В Poetry есть основная группа зависимостей — `main`.

Также можно создавать дополнительные группы:

* `dev`
* `lint`
* `test`
* и другие

### Установить только dev и lint

```bash
poetry install --only dev,lint
```

### Установить main и dev

```bash
poetry install --only main,dev
```

### Установить main и lint

```bash
poetry install --only main,lint
```

### Установить всё, кроме dev и lint

```bash
poetry install --without dev,lint
```

> Важно: группы указываются через запятую, без пробела.

Правильно:

```bash
poetry install --without dev,lint
```

Неправильно:

```bash
poetry install --without dev lint
```

---


