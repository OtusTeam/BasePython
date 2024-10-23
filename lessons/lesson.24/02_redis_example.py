import redis
import time

# Подключение к локальному Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Проверка подключения с помощью команды PING
if r.ping():
    print("Подключение к Redis успешно!")
else:
    print("Ошибка подключения!")

# 2. Работа со строками: SET, GET, EXPIRE

# Устанавливаем ключ 'username' со значением 'Alice'
r.set('username', 'Alice')

# Получаем значение ключа 'username' и выводим его
user = r.get('username')
print(f"Имя пользователя: {user.decode()}")  # Расшифровываем байты в строку

# Устанавливаем время жизни ключа 'username' на 5 секунд
r.expire('username', 5)
print("Ключ 'username' будет удален через 5 секунд.")

# Ожидание 5 секунд, чтобы убедиться, что ключ удален
time.sleep(5)

# Проверяем, существует ли ключ после истечения времени
if not r.exists('username'):
    print("Ключ 'username' больше не существует.")

# 3. Работа со счетчиками: INCR, DECR

# Устанавливаем счетчик просмотров страницы с начальным значением 0
r.set('page_views', 0)

# Получаем текущее значение счетчика и выводим его
views = r.get('page_views')
print(f"Количество просмотров страницы: {views.decode()}")

# Ждем 1 секунду для демонстрации постепенного увеличения счетчика
time.sleep(1)

# Увеличиваем счетчик на 1
r.incr('page_views')
views = r.get('page_views')
print(f"Количество просмотров страницы: {views.decode()}")
time.sleep(1)

# Еще раз увеличиваем счетчик на 1
r.incr('page_views')
views = r.get('page_views')
print(f"Количество просмотров страницы: {views.decode()}")
time.sleep(1)

# Еще одно увеличение счетчика
r.incr('page_views')
views = r.get('page_views')
print(f"Количество просмотров страницы: {views.decode()}")
time.sleep(1)

# Уменьшаем счетчик на 1 (например, когда пользователь ушел со страницы)
r.decr('page_views')
views = r.get('page_views')
print(f"Количество просмотров страницы после уменьшения: {views.decode()}")

# 4. Работа со списками: LPUSH, RPUSH, LPOP

# Добавляем задачи в начало и конец списка
r.lpush('task_queue', 'Task 1')  # Добавляем в начало
r.rpush('task_queue', 'Task 2')  # Добавляем в конец
r.lpush('task_queue', 'Task 0')  # Добавляем еще одну задачу в начало

# Получаем все элементы списка (от начала до конца) и выводим их
tasks = r.lrange('task_queue', 0, -1)  # lrange(0, -1) возвращает весь список
print(f"Текущие задачи в очереди: {[task.decode() for task in tasks]}")  # Декодируем байты

# Удаляем и возвращаем первый элемент из списка (FIFO)
first_task = r.lpop('task_queue')
print(f"Первая выполненная задача: {first_task.decode()}")

# Снова выводим оставшиеся задачи в списке
tasks = r.lrange('task_queue', 0, -1)
print(f"Оставшиеся задачи: {[task.decode() for task in tasks]}")

# 5. Работа с хэшами: HSET, HGET, HDEL

# Добавляем данные пользователя в хэш
r.hset('user:1000', 'name', 'Alice')   # Устанавливаем поле 'name' со значением 'Alice'
r.hset('user:1000', 'age', 30)         # Устанавливаем поле 'age' со значением 30
r.hset('user:1000', 'email', 'alice@example.com')  # Добавляем email

# Получаем значения полей 'name' и 'age' из хэша
user_name = r.hget('user:1000', 'name')
user_age = r.hget('user:1000', 'age')
print(f"Имя: {user_name.decode()}, Возраст: {user_age.decode()}")

# Удаляем поле 'email' из хэша
r.hdel('user:1000', 'email')

# Проверяем, что поле 'email' было удалено
email = r.hget('user:1000', 'email')
if not email:
    print("Поле 'email' было удалено.")

# 6. Удаление ключей: DEL

# Создаем временный ключ со значением 'Temporary Value'
r.set('temp_key', 'Temporary Value')
print(f"Ключ 'temp_key' создан: {r.get('temp_key').decode()}")

# Удаляем ключ 'temp_key'
r.delete('temp_key')

# Проверяем, существует ли ключ после удаления
if not r.exists('temp_key'):
    print("Ключ 'temp_key' был успешно удален.")
