# Generated by Django 3.2.4 on 2021-07-06 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_session', '0002_trainingsession_minimum_number_of_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingsession',
            name='required_materials',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Liste de materiel'),
        ),
    ]