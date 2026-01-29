python -m venv ./.myvenv
source ./.venv/bin/activate
./.venv/Scripts/activate
./.venv/Scripts/activate.ps1


# Установка pytest
pip install pytest


# Запуск pytest
pytest 
pytest -vv 
pytest ./tests -vv
pytest ./tests/test_calc.py -vv
pytest ./tests/test_calc.py::test_add -vv

# Покрытие тестами
pip install pytest-cov