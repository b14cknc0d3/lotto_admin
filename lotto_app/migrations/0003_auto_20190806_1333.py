# Generated by Django 2.1.11 on 2019-08-06 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotto_app', '0002_auto_20190806_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fivel',
            name='is_winner',
            field=models.CharField(default=0, max_length=1, verbose_name='is lottery winner'),
        ),
        migrations.AlterField(
            model_name='onel',
            name='is_winner',
            field=models.CharField(default=0, max_length=1, verbose_name='is lottery winner'),
        ),
        migrations.AlterField(
            model_name='twol',
            name='is_winner',
            field=models.CharField(default=0, max_length=1, verbose_name='is lottery winner'),
        ),
    ]
