# Generated by Django 4.2.3 on 2023-07-29 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diet_App', '0006_remove_information_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breakfast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(default=None, max_length=100, null=True)),
                ('Food1', models.CharField(default=None, max_length=100, null=True)),
                ('Food2', models.CharField(default=None, max_length=100, null=True)),
                ('Food3', models.CharField(default=None, max_length=100, null=True)),
                ('Food4', models.CharField(default=None, max_length=100, null=True)),
                ('Food5', models.CharField(default=None, max_length=100, null=True)),
                ('Food6', models.CharField(default=None, max_length=100, null=True)),
                ('Food7', models.CharField(default=None, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Breakfast',
            },
        ),
    ]
