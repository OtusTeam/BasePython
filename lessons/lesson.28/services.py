from models import Owner, Pet, Vaccine, Stock
from database import Session
from sqlalchemy import func

# 1. Функция для получения всех прививок и животных, которым они проставлены
"""
Функция `get_all_vaccines_and_pets` извлекает все записи о прививках из таблицы `Vaccine`. 
Затем для каждой прививки через связь many-to-many с таблицей `Pet` выводится список всех животных, 
которым была сделана эта прививка. Здесь используется связь `many-to-many` для получения связанных данных.
"""
def get_all_vaccines_and_pets():
    session = Session()
    vaccines = session.query(Vaccine).all()
    for vaccine in vaccines:
        print(f"Vaccine: {vaccine.name}")
        for pet in vaccine.pets:
            print(f"  - Pet: {pet.name} (Species: {pet.species})")
    session.close()


# 2. Функция для получения всех животных и прививок, которые им сделаны
"""
Функция `get_all_pets_and_vaccines` извлекает все записи о животных из таблицы `Pet`. 
Затем для каждого животного через связь many-to-many с таблицей `Vaccine` выводится список всех прививок, 
которые были сделаны этому животному. Связь many-to-many позволяет легко получить все прививки для каждого животного.
"""
def get_all_pets_and_vaccines():
    session = Session()
    pets = session.query(Pet).all()
    for pet in pets:
        print(f"Pet: {pet.name} (Species: {pet.species})")
        for vaccine in pet.vaccines:
            print(f"  - Vaccine: {vaccine.name}")
    session.close()


# 3. Функция для получения всех владельцев, их животных и прививок, сделанных этим животным
"""
Функция `get_all_owners_with_pets_and_vaccines` извлекает всех владельцев из таблицы `Owner`. 
Затем для каждого владельца выводится список его животных, а для каждого животного выводится список прививок, 
сделанных этому животному. Используется иерархическая структура отношений (владелец -> животное -> прививки) 
для получения и отображения всех данных.
"""
def get_all_owners_with_pets_and_vaccines():
    session = Session()
    owners = session.query(Owner).all()
    for owner in owners:
        print(f"Owner: {owner.name}")
        for pet in owner.pets:
            print(f"  - Pet: {pet.name} (Species: {pet.species})")
            for vaccine in pet.vaccines:
                print(f"    - Vaccine: {vaccine.name}")
    session.close()


# 4. Функция для получения всех владельцев, которые участвуют в акциях
"""
Функция `get_all_owners_in_stocks` использует `JOIN` для соединения таблицы `Owner` с таблицей `Stock` через промежуточную таблицу. 
Она выбирает только тех владельцев, которые участвуют хотя бы в одной акции. Используя `join`, функция получает всех владельцев, 
имеющих связь с какой-либо акцией, и выводит их имена.
"""
def get_all_owners_in_stocks():
    session = Session()
    owners = session.query(Owner).join(Owner.stocks).all()
    for owner in owners:
        print(f"Owner: {owner.name}")
    session.close()


# 5. Функция для получения всех акций и владельцев, которые в них участвуют
"""
Функция `get_all_stocks_and_owners` извлекает все акции из таблицы `Stock`. 
Затем для каждой акции через связь many-to-many с таблицей `Owner` выводится список всех владельцев, 
участвующих в этой акции. Функция демонстрирует использование связи many-to-many для извлечения данных 
из обеих связанных таблиц.
"""
def get_all_stocks_and_owners():
    session = Session()
    stocks = session.query(Stock).all()
    for stock in stocks:
        print(f"Stock: {stock.name} (Price: {stock.price})")
        for owner in stock.owners:
            print(f"  - Owner: {owner.name}")
    session.close()


# 6. Функция для получения всех животных, владельцы которых участвуют в акциях
"""
Функция `get_pets_of_owners_in_stocks` использует `JOIN` для соединения таблицы `Owner` с таблицей 
`Stock` через промежуточную таблицу. 
Она выбирает только тех владельцев, которые участвуют в акциях, и затем выводит список их животных. 
Используя иерархическое отношение (владелец -> животные), функция позволяет получить всех животных, 
владельцы которых связаны с акциями.
"""
def get_pets_of_owners_in_stocks():
    session = Session()
    owners = session.query(Owner).join(Owner.stocks).all()
    for owner in owners:
        print(f"Owner: {owner.name}")
        for pet in owner.pets:
            print(f"  - Pet: {pet.name} (Species: {pet.species})")
    session.close()


# 7. Функция для получения всех владельцев, которые не сделали ни одной прививки своим животным
"""
Функция `get_owners_without_vaccinated_pets` выбирает всех владельцев из таблицы `Owner`. 
Затем для каждого владельца проверяется, есть ли у его животных хотя бы одна прививка. 
Если у всех животных владельца нет прививок, его имя выводится. Таким образом, 
функция фильтрует владельцев, у которых нет привитых животных.
"""
def get_owners_without_vaccinated_pets():
    session = Session()
    owners = session.query(Owner).all()
    for owner in owners:
        vaccinated = False
        for pet in owner.pets:
            if pet.vaccines:
                vaccinated = True
                break
        if not vaccinated:
            print(f"Owner: {owner.name}")
    session.close()


# 8. Функция для получения всех владельцев, которые не участвуют в акциях
"""
Функция `get_owners_not_in_stocks` использует `OUTER JOIN` для соединения таблицы `Owner` с таблицей `Stock` через промежуточную таблицу. 
Затем применяется фильтр `Stock.id == None`, чтобы выбрать только тех владельцев, которые не имеют связи с акциями. 
Функция выводит имена владельцев, которые не участвуют ни в одной акции.
"""
def get_owners_not_in_stocks():
    session = Session()
    owners = session.query(Owner).outerjoin(Owner.stocks).filter(Stock.id == None).all()
    for owner in owners:
        print(f"Owner: {owner.name}")
    session.close()


# 9. Функция для получения всех владельцев, которые участвуют сразу в двух или более акциях
"""
Функция `get_owners_in_multiple_stocks` использует группировку и агрегатную функцию `count` для подсчета количества акций, 
в которых участвует каждый владелец. С помощью фильтрации по количеству акций, больше или равно 2, 
функция извлекает только тех владельцев, которые участвуют сразу в двух или более акциях.
"""
def get_owners_in_multiple_stocks():
    session = Session()
    owners_in_multiple_stocks = (
        session.query(Owner)
        .join(Owner.stocks)
        .group_by(Owner.id)
        .having(func.count(Stock.id) >= 2)
        .all()
    )
    for owner in owners_in_multiple_stocks:
        print(f"Owner: {owner.name}")
    session.close()


# 10. Функция для получения всех животных, которые имеют две и более прививок
"""
Функция `get_pets_with_multiple_vaccines` использует группировку и агрегатную функцию `count` для подсчета количества прививок, 
которые были сделаны каждому животному. С помощью фильтрации по количеству прививок, больше или равно 2, 
функция извлекает только тех животных, которые имеют две и более прививок одновременно.
"""
def get_pets_with_multiple_vaccines():
    session = Session()
    pets_with_multiple_vaccines = (
        session.query(Pet)
        .join(Pet.vaccines)
        .group_by(Pet.id)
        .having(func.count(Vaccine.id) >= 2)
        .all()
    )
    for pet in pets_with_multiple_vaccines:
        print(f"Pet: {pet.name} (Species: {pet.species})")
    session.close()


# 11. Функция для получения всех владельцев, которые участвуют в двух или более указанных акциях
"""
Функция `get_owners_in_multiple_stocks` принимает переменное количество аргументов акций и 
выбирает владельцев, которые участвуют как минимум в двух из этих акций. 
Функция использует `JOIN` и `GROUP BY` для фильтрации владельцев по количеству акций, в которых они участвуют.
"""
def get_owners_in_multiple_stocks(*stocks):
    session = Session()
    owners_in_multiple_stocks = (
        session.query(Owner)
        .join(Owner.stocks)
        .filter(Stock.name.in_(stocks))
        .group_by(Owner.id)
        .having(func.count(Stock.id) >= 2)
        .all()
    )
    for owner in owners_in_multiple_stocks:
        print(f"Owner: {owner.name}")
    session.close()


# 12. Функция для получения всех животных, которые имеют две и более указанных прививок
"""
Функция `get_pets_with_multiple_vaccines` принимает переменное количество аргументов прививок и 
выбирает животных, которым сделали как минимум две из этих прививок. 
Функция использует `JOIN` и `GROUP BY` для фильтрации животных по количеству прививок.
"""
def get_pets_with_multiple_vaccines(*vaccines):
    session = Session()
    pets_with_multiple_vaccines = (
        session.query(Pet)
        .join(Pet.vaccines)
        .filter(Vaccine.name.in_(vaccines))
        .group_by(Pet.id)
        .having(func.count(Vaccine.id) >= 2)
        .all()
    )
    for pet in pets_with_multiple_vaccines:
        print(f"Pet: {pet.name} (Species: {pet.species})")
    session.close()


# Вызов функций для тестирования
# get_all_vaccines_and_pets()
# get_all_pets_and_vaccines()
# get_all_owners_with_pets_and_vaccines()
# get_all_owners_in_stocks()
# get_all_stocks_and_owners()
# get_pets_of_owners_in_stocks()
# get_owners_without_vaccinated_pets()
# get_owners_not_in_stocks()
# get_owners_in_multiple_stocks()
# get_pets_with_multiple_vaccines('Rabies', 'Distemper')