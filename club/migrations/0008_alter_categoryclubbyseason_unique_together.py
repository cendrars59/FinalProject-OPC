# Generated by Django 3.2.2 on 2021-05-19 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0007_auto_20210519_2353'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='categoryclubbyseason',
            unique_together={('club', 'category', 'season')},
        ),
    ]
