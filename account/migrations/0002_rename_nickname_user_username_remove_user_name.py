# Generated by Django 4.2.13 on 2024-05-11 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='nickname',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
