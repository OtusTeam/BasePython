import unittest
from unittest.mock import Mock, mock_open, patch
from file_example import FileService

class TestFileService(unittest.TestCase):

    def setUp(self):
        # Создаем mock-объект для file_reader
        self.file_reader = Mock()
        self.service = FileService(self.file_reader)

    @patch('builtins.open', new_callable=mock_open, read_data='file content')
    def test_read_file(self, mock_file):
        file_path = 'test.txt'

        # Настраиваем mock-объект для метода open
        self.file_reader.open = mock_file
        content = self.service.read_file(file_path)

        # Проверяем, что содержимое файла соответствует ожиданиям
        self.assertEqual(content, 'file content')
        # Проверяем, что метод open был вызван с правильными параметрами
        self.file_reader.open.assert_called_with(file_path, 'r')

if __name__ == "__main__":
    unittest.main()
