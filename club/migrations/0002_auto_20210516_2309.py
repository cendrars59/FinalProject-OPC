# Generated by Django 3.2.2 on 2021-05-16 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32, unique=True)),
                ('label', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(default='Ajoutez ici la decription du rôle', null=True)),
                ('color_code', models.CharField(max_length=32)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32, unique=True)),
                ('label', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(default='Ajoutez ici la decription du rôle', null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32, unique=True)),
                ('label', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(default='Ajoutez ici la decription du rôle', null=True)),
                ('yob', models.IntegerField()),
                ('yoe', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_current', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='tag',
            field=models.CharField(default='A définir', max_length=128),
        ),
    ]