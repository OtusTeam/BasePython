### Домашнее задание: Реализация CRUD-операций с CSV-файлом через WSGI (по просьбам учеников, для закрепления материала, необязательно к исполнению)

Необходимо разработать WSGI-приложение, которое выполняет операции с данными, хранящимися в CSV-файле. Реализуйте шесть операций:

---

### Основные операции:

1. **Чтение всех записей (GET /records):**
   - Вернуть все записи из CSV-файла в формате JSON.

2. **Создание записи (POST /records):**
   - Добавить новую запись в CSV-файл.
   - Данные передаются в теле запроса в формате JSON.

3. **Обновление записи (PUT /records/{id}):**
   - Обновить запись с указанным `id` в CSV-файле.
   - Новые данные передаются в теле запроса в формате JSON.

4. **Удаление записи (DELETE /records/{id}):**
   - Удалить запись с указанным `id` из CSV-файла.

---

### Дополнительные операции:

5. **Сортировка записей (GET /records/sort):**
   - Вернуть записи, отсортированные по указанному полю (например, `name`, `age`, `city`).
   - Сортировка задаётся через параметры запроса:
     - `field`: имя поля для сортировки (обязательно).
     - `order`: направление (`asc` или `desc`, по умолчанию `asc`).

6. **Удаление всех записей с определённым `id` (DELETE /records/remove_by_id):**
   - Удалить все записи с указанным `id`, переданным в теле запроса.

---

### Формат CSV-файла:

CSV-файл должен содержать следующие столбцы:
- `id`: Уникальный идентификатор записи.
- `name`: Имя человека.
- `age`: Возраст.
- `city`: Город.

Пример содержимого `data.csv`:
```
id,name,age,city
1,Alice,30,New York
2,Bob,25,Los Angeles
3,Alice,22,Chicago
```

---