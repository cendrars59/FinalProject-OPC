# Generated by Django 3.2.4 on 2021-06-09 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210609_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='additional_information',
            new_name='about',
        ),
    ]
