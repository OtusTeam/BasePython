# Используем __all__ для экспорта моделей
__all__ = ["Owner", "Pet", "Visit", "MedicalRecord", "Base"]

from .models import Owner, Pet, Visit, MedicalRecord, Base
