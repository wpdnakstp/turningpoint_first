# Generated by Django 2.1.8 on 2019-07-21 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turningaccounts', '0003_auto_20190721_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turninguser',
            name='tnPhoneNumb',
            field=models.CharField(max_length=13),
        ),
    ]
