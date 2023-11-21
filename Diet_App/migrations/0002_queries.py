# Generated by Django 4.2.3 on 2023-07-18 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diet_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_id', models.CharField(default=None, max_length=100, null=True)),
                ('Query', models.CharField(default=None, max_length=300, null=True)),
                ('Answer', models.CharField(default=None, max_length=300, null=True)),
            ],
            options={
                'db_table': 'UserFeedback',
            },
        ),
    ]
