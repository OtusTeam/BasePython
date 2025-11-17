## windows   
python -m venv ./.venv   
   
## Linux/mac   
python3 -m venv ./.myvenv    
   
## Активация в Linux/mac   
source ./.venv/bin/activate   
   
## Активация в windows   
./.venv/bin/activate  # cmd   
./.venv/bin/Activate.ps1  # PowerShell   
   
## Дективация    
deactivate   
   
## Установить   
pip install pytest   
pip install pytest-mock   
pip install pytest-cov   
   
## Сгенерировать html отчет   
pytest --cov=src.my_math --cov-report=html   
   
