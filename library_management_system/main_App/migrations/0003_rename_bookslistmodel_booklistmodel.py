# Generated by Django 4.0.5 on 2023-01-13 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_App', '0002_rename_authorlist_authorlistmodel_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='booksListModel',
            new_name='bookListModel',
        ),
    ]
