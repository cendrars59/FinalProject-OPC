# Generated by Django 3.2.2 on 2021-05-20 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0010_alter_season_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='label',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='season',
            name='label',
            field=models.CharField(max_length=128, null=True),
        ),
    ]