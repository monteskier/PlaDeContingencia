# Generated by Django 2.0.2 on 2018-02-09 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pla', '0002_seguiment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actiu',
            name='servei',
        ),
        migrations.AddField(
            model_name='actiu',
            name='servei',
            field=models.ManyToManyField(to='pla.Servei'),
        ),
    ]
