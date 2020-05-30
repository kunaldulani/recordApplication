# Generated by Django 3.0.6 on 2020-05-29 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordApp', '0003_auto_20200529_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.ForeignKey(on_delete=models.SET('Status Deleted'), related_name='statusName', to='recordApp.Status'),
        ),
    ]