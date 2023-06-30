"""
Django подход

Fat models
Thin views
Stupid templates

MVC - model, view, controller
“MTV” framework – that is, “model”, “template”, and “view.”
"""
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ("celery_app",)
