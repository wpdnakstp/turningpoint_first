# Generated by Django 2.1.8 on 2019-08-03 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turningaccounts', '0005_auto_20190803_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='turninguser',
            name='userFullName',
            field=models.CharField(default='', max_length=20),
        ),
    ]
