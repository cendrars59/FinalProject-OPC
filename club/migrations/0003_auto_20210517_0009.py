# Generated by Django 3.2.2 on 2021-05-16 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_auto_20210516_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32, unique=True)),
                ('label', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(default='Ajoutez ici la decription de la division', null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='season',
            name='description',
            field=models.TextField(default='Ajoutez ici la decription de las saison', null=True),
        ),
    ]
