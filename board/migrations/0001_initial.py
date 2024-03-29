# Generated by Django 2.2.2 on 2019-06-05 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=None)),
                ('image_name', models.CharField(default=None, max_length=255)),
                ('start_date', models.DateTimeField(default=None, max_length=255)),
                ('stop_date', models.DateTimeField(default=None, max_length=255)),
                ('urgent', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='text',
            fields=[
                ('text_id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(default=None, max_length=255)),
                ('start_date', models.DateTimeField(default=None, max_length=255)),
                ('stop_date', models.DateTimeField(default=None, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(default=None, max_length=255)),
                ('username', models.CharField(default=None, max_length=255)),
                ('email', models.CharField(default=None, max_length=255)),
                ('department', models.CharField(default=None, max_length=255)),
                ('password', models.CharField(default=None, max_length=255)),
            ],
        ),
    ]
