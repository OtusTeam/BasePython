import psycopg2

# Подключение к PostgreSQL
conn = psycopg2.connect(
    dbname="mydb",
    user="postgres",
    password="password",
    host="localhost"
)

# Создаем курсор для выполнения SQL-запросов
cursor = conn.cursor()

# Проверим подключение
print("Подключение к базе данных успешно установлено!")

# 2. Создание таблицы
create_table_query = '''
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(50)
)
'''
cursor.execute(create_table_query)
conn.commit()
print("Таблица students успешно создана!")

# 3. Вставка данных
insert_query = '''
INSERT INTO students (name, age, course) VALUES (%s, %s, %s)
'''
# Вставляем одного студента
student_data = ('Alice', 22, 'Math')
cursor.execute(insert_query, student_data)

# Вставляем нескольких студентов
students = [
    ('Bob', 24, 'Physics'),
    ('Charlie', 21, 'Chemistry')
]
cursor.executemany(insert_query, students)
conn.commit()
print("Данные успешно вставлены!")

# 4. Запрос данных (SELECT)
select_query = 'SELECT * FROM students'
cursor.execute(select_query)
students = cursor.fetchall()
print("Список студентов:")
for student in students:
    print(student)

# 5. Обновление данных
update_query = '''
UPDATE students
SET age = %s
WHERE name = %s
'''
cursor.execute(update_query, (23, 'Alice'))
conn.commit()
print("Данные успешно обновлены!")

# 6. Удаление данных
delete_query = '''
DELETE FROM students WHERE name = %s
'''
cursor.execute(delete_query, ('Bob',))
conn.commit()
print("Студент успешно удален!")

# 7. Работа с транзакциями
try:
    print("Начало транзакции")
    cursor.execute(insert_query, ('David', 25, 'Biology'))
    
    # Принудительная ошибка для демонстрации отката транзакции
    raise Exception("Ошибка для демонстрации отката транзакции")
    
    conn.commit()
    print("Транзакция успешно завершена!")

except Exception as e:
    conn.rollback()
    print(f"Транзакция откатена. Причина: {e}")

# 8. Закрытие соединения
cursor.close()
conn.close()
print("Соединение с базой данных закрыто.")
