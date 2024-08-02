import unittest
from unittest.mock import Mock
from db_example import UserService

class TestUserService(unittest.TestCase):

    def setUp(self):
        # Создаем mock-объект для db_client
        self.db_client = Mock()
        self.service = UserService(self.db_client)

    def test_add_user(self):
        # Определяем параметры для теста
        user_id = "123"
        user_data = {"name": "John Doe"}

        # Вызываем метод add_user
        self.service.add_user(user_id, user_data)

        # Проверяем, что метод insert был вызван с правильными параметрами
        self.db_client.insert.assert_called_with(user_id, user_data)

    def test_get_user(self):
        user_id = "123"
        user_data = {"name": "John Doe"}
        # Настраиваем mock-объект для метода find
        self.db_client.find.return_value = user_data

        # Вызываем метод get_user
        result = self.service.get_user(user_id)

        # Проверяем, что результат соответствует ожиданиям
        self.assertEqual(result, user_data)
        # Проверяем, что метод find был вызван с правильными параметрами
        self.db_client.find.assert_called_with(user_id)

if __name__ == "__main__":
    unittest.main()
