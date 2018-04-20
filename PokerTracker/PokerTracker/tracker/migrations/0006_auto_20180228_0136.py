# Generated by Django 2.0.2 on 2018-02-28 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_session_hourly_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a place where you played your session', max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='session',
            name='hours',
        ),
        migrations.RemoveField(
            model_name='session',
            name='minutes',
        ),
        migrations.AddField(
            model_name='session',
            name='place',
            field=models.ManyToManyField(help_text='Select a place for this session', to='tracker.Place'),
        ),
    ]