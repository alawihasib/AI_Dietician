# Generated by Django 4.2.3 on 2023-07-29 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Diet_App', '0007_breakfast'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Breakfast',
            new_name='Breakfast_List',
        ),
        migrations.AlterModelTable(
            name='breakfast_list',
            table='Breakfast_List',
        ),
    ]
