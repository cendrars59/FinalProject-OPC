# Generated by Django 3.2.4 on 2021-07-06 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_session', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingsession',
            name='minimum_number_of_people',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]