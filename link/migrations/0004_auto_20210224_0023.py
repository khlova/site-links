# Generated by Django 3.1.4 on 2021-02-23 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0003_auto_20210113_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='short_link',
            field=models.CharField(max_length=30, verbose_name='Сокращенная ссылка'),
        ),
    ]
