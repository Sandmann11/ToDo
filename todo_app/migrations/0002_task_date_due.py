# Generated by Django 3.1.7 on 2021-04-25 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_due',
            field=models.DateTimeField(null=True),
        ),
    ]