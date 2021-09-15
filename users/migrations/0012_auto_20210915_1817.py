# Generated by Django 3.2.5 on 2021-09-15 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0012_auto_20210727_2146'),
        ('users', '0011_auto_20210915_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='involvedasicategoryforseason',
            name='club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='club.club'),
        ),
        migrations.AlterField(
            model_name='involvedasicategoryforseason',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.role'),
        ),
        migrations.AlterField(
            model_name='involvedasicategoryforseason',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='club.season', verbose_name='Saison'),
        ),
    ]
