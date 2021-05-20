# Generated by Django 3.2.2 on 2021-05-19 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0005_remove_season_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32, unique=True)),
                ('label', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(default='Ajoutez ici la decription de la catégorie', null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_main', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=1024)),
                ('main_phone', models.CharField(max_length=10)),
                ('main_email', models.CharField(max_length=128, unique=True)),
                ('main_contact', models.CharField(max_length=128, unique=True)),
                ('main_color_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32, unique=True)),
                ('label', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(default='Ajoutez ici la decription de la division', null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('rank', models.IntegerField(default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
