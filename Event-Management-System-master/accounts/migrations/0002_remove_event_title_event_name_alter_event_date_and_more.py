# Generated by Django 5.0.7 on 2024-07-27 12:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='title',
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default='Default Event Name', max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]