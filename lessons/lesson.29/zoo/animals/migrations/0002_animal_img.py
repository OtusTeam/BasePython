# Generated by Django 3.2.4 on 2021-06-25 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='animals'),
        ),
    ]