# Generated by Django 3.2.3 on 2021-07-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0028_auto_20210725_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
    ]