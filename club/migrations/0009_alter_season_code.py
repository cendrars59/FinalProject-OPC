# Generated by Django 3.2.2 on 2021-05-19 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0008_alter_categoryclubbyseason_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='code',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
