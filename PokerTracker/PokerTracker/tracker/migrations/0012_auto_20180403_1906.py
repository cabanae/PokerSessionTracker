# Generated by Django 2.0.2 on 2018-04-04 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0011_auto_20180302_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='Notes',
            field=models.TextField(blank=True, help_text='Enter some notes on the session', max_length=1000),
        ),
    ]