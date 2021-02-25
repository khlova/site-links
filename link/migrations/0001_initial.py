# Generated by Django 3.1.5 on 2021-01-12 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_link', models.CharField(max_length=200)),
                ('short_link', models.CharField(max_length=30)),
            ],
        ),
    ]