# Generated by Django 3.2.5 on 2021-07-28 21:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_additional_information_customuser_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.UUIDField(default=uuid.uuid4)),
                ('label', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(default='Ajoutez ici la decription du rôle', null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]