# Generated by Django 2.2.2 on 2019-06-05 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20190605_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='start_date',
            field=models.DateTimeField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='images',
            name='stop_date',
            field=models.DateTimeField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='images',
            name='urgent',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
