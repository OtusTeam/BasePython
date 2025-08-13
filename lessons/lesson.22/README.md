python3 -m venv myvenv
source ./.venv/bin/activate
deactivate

pip --version
pip list

pip install requests
pip uninstall requests
pip install --upgrade requests

pip freeze > requirements.txt
pip install -r ./requirements.txt

poetry --version

poetry init

poetry new my_project

Добавляет зависимость
poetry add requests
poetry add requests@2.31.0
poetry add --dev ruff

poetry remove requests - удаляет зависимость

poetry install - устанавливает все зависимости из pyproject.toml

poetry update requests

poetry list
poetry help


poetry show
poetry show fastapi

