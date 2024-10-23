from pymongo import MongoClient

# Подключение к локальному MongoDB
client = MongoClient('localhost', 27017)

# Выбор или создание базы данных
db = client['school']

# Создание или выбор коллекции 'students'
students = db['students']

# 1. Вставка документов
def insert_documents():
    student1 = {"name": "Alice", "age": 22, "course": "Math"}
    student2 = {"name": "Bob", "age": 24, "course": "Physics"}
    
    # Вставляем документы
    result = students.insert_many([student1, student2])
    print(f"Inserted document IDs: {result.inserted_ids}")

# 2. Поиск документов
def find_documents():
    # Находим всех студентов
    all_students = students.find()
    print("Все студенты:")
    for student in all_students:
        print(student)
    
    # Поиск студента по имени
    alice = students.find_one({"name": "Alice"})
    print("\nНайден студент с именем Alice:")
    print(alice)

# 3. Обновление документа
def update_document():
    # Обновим возраст студента Alice
    result = students.update_one({"name": "Alice"}, {"$set": {"age": 23}})
    print(f"\nUpdated {result.modified_count} document(s)")

    # Проверим результат обновления
    updated_alice = students.find_one({"name": "Alice"})
    print("Обновленные данные студента Alice:")
    print(updated_alice)

# 4. Удаление документа
def delete_document():
    # Удалим студента по имени Bob
    result = students.delete_one({"name": "Bob"})
    print(f"\nDeleted {result.deleted_count} document(s)")

    # Проверим, что Bob был удален
    remaining_students = students.find()
    print("Оставшиеся студенты после удаления:")
    for student in remaining_students:
        print(student)

# Выполняем операции
print("1. Вставка документов:")
insert_documents()

print("\n2. Поиск документов:")
find_documents()

print("\n3. Обновление документа:")
update_document()

print("\n4. Удаление документа:")
delete_document()
