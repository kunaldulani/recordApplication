# Generated by Django 3.0.6 on 2020-05-29 22:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recordApp', '0002_auto_20200529_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='dateApplied',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
