# Generated by Django 3.2.5 on 2021-07-26 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_plan', '0002_auto_20210726_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingplanattenderslist',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]