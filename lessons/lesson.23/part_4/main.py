from services import get_visits_by_owner, filter_visits_by_date_range
from database import create_all

if __name__ == "__main__":
    # Создаем таблицы в базе данных
    create_all()
    
    # Примеры выполнения запросов
    print("Visits by Owner 'Alice Johnson':")
    get_visits_by_owner("Alice Johnson")
    
    print("\nVisits in Date Range '2024-01-01' to '2024-03-31':")
    filter_visits_by_date_range("2024-01-01", "2024-03-31")
