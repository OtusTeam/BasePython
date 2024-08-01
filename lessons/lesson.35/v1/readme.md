## Инструкция

В корне проекта выполните команды

```
flask db init
flask db migrate
flask db upgrade
```

Иногда команды не срабатывают, тогда вводите их следующим образом

```
python3 -m flask db init
python3 -m flask db migrate
python3 -m flask db upgrade
```

Если приложение не запускается, то убедитесь, что переменная окружения FLASK_APP указывает на ваш файл инициализации приложения:


В Linux/MacOS:
```bash
export FLASK_APP=main.py
export PYTHONPATH=$(pwd)
```

В Windows:
```cmd
set FLASK_APP=main.py
```
Для добавления записей
- Откройте оболочку Flask:
```bash
flask shell
```
- Добавьте несколько записей:
```python
from models.models import db, Owner, Pet
# Добавление владельцев
owner1 = Owner(name='John Doe', age=30, phone='1234567890')
owner2 = Owner(name='Jane Smith', age=25, phone='0987654321')
db.session.add(owner1)
db.session.add(owner2)
db.session.commit()
# Добавление животных
pet1 = Pet(name='Buddy', breed='Dog', age=3, owner_id=owner1.id)
pet2 = Pet(name='Mittens', breed='Cat', age=2, owner_id=owner1.id)
pet3 = Pet(name='Charlie', breed='Parrot', age=4)
db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)
db.session.commit()
```