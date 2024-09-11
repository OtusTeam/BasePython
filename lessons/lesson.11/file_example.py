class FileService:
    def __init__(self, file_reader):
        # file_reader — это объект, который взаимодействует с файловой системой
        self.file_reader = file_reader

    def read_file(self, file_path):
        # Метод чтения содержимого файла
        with self.file_reader.open(file_path, 'r') as file:
            return file.read()
