# Generated by Django 2.1.8 on 2019-07-21 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turningaccounts', '0002_turninguser_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turninguser',
            name='nickName',
            field=models.CharField(default='random', max_length=20),
        ),
    ]
