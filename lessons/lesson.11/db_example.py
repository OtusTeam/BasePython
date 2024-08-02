class UserService:
    def __init__(self, db_client):
        # db_client — это объект, который взаимодействует с базой данных
        self.db_client = db_client

    def add_user(self, user_id, user_data):
        # Метод добавления пользователя в базу данных
        self.db_client.insert(user_id, user_data)

    def get_user(self, user_id):
        # Метод получения данных пользователя из базы данных
        return self.db_client.find(user_id)
