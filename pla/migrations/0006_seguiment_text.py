# Generated by Django 2.0.2 on 2018-02-16 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pla', '0005_auto_20180209_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='seguiment',
            name='text',
            field=models.TextField(default='Sense intervencions'),
            preserve_default=False,
        ),
    ]