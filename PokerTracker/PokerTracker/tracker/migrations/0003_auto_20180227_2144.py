# Generated by Django 2.0.2 on 2018-02-28 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_remove_session_hero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='session_date',
        ),
        migrations.RemoveField(
            model_name='session',
            name='time_end',
        ),
        migrations.AddField(
            model_name='session',
            name='hours',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='minutes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='time_start',
            field=models.DateTimeField(),
        ),
    ]
