# Generated by Django 4.2.1 on 2023-05-08 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_alter_friendship_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='status',
            field=models.IntegerField(choices=[(-1, 'Исходящая заявка'), (1, 'Входящая заявка'), (0, 'Друзья')]),
        ),
    ]
