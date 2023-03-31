__all__ = ("app",)

from main import app

# Django:
# fat models -> всю логику складывать в модели
# thin views -> минимум логики в view функциях
# stupid templates -> никакой логики в шаблонах
