# Generated by Django 3.2.2 on 2021-05-19 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0006_auto_20210519_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryClubBySeason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(default='Ajoutez ici la decription de la catégorie', null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_current', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.category')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.club')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.season')),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='categories',
            field=models.ManyToManyField(through='club.CategoryClubBySeason', to='club.Category'),
        ),
        migrations.AddField(
            model_name='club',
            name='seasons',
            field=models.ManyToManyField(through='club.CategoryClubBySeason', to='club.Season'),
        ),
    ]
