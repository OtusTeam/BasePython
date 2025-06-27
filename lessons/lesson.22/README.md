python3 -m venv myvenv
source ./myvenv/bin/activate
deactivate

pip --version
pip list

pip install requests
pip install requests==2.26.0

pip install --upgrade requests
pip uninstall requests

pip freeze > requirements.txt
pip install -r requirements.txt


poetry --version

# Инициализация проекта
poetry init 

# Добавить зависимость 
poetry add requests

# Добавить конкретную версию зависимости 
poetry add requests@2.26.0

# Добавить конкретную версию зависимости из диапазона
poetry add "requests>=2.26.0,<2.29"

# Удалить зависимость 
poetry remove flask

# Добавить в группу нашу зависимость 
poetry add --dev ptest
poetry add --group link ruff

# Обновить зависимость 
poetry update requests

# Установить зависимости 
poetry install
poetry install --without dev
poetry install --only link

poetry env info
poetry env list

poetry cache clear -all pypi
