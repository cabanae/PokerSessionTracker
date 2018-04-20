# Generated by Django 2.0.2 on 2018-03-03 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_auto_20180301_0315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_type', models.CharField(help_text='Enter game type of your session', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='session',
            name='time_per_session',
            field=models.DurationField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='game_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tracker.Game'),
        ),
    ]
