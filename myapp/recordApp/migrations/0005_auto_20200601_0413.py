# Generated by Django 3.0.6 on 2020-06-01 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordApp', '0004_auto_20200529_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='attendeeEmail',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='reminderDate',
            field=models.DateField(blank=True, default='2000-01-01', null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='reminderNote',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]
