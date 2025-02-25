poetry new - создать новый проект  
poetry init  - инициализация poetry  
poetry add flask - добавить пакет  
poetry install - установка зависимостей  
poetry update - обновление зависимостей  
poetry remove flask - удалить пакет  
poetry env info - информация о окружении  
poetry install --without dev lint - установка зависимостей без dev, lint  
poetry install --only dev - установка зависимостей только dev  
poetry add --group lint black - добавить пакет в группу lint  
poetry cache clear --all - очистить кэш pypi  
  
flask (>3.1.2,<3.2.0)  
flask (^3.1.20)   - flask (>3.1.20,<4.0.0)  
flask (~3.1.20)   - flask (>3.1.20,<3.2.0)  
flask (3.1.*)   - flask (>3.1.20,<3.2.0)  
flask (^3.1.20 || ^4.2.2)  - логическая ИЛИ  
  
3.1.0  
  
