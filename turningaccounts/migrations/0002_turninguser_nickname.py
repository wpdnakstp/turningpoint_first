# Generated by Django 2.1.8 on 2019-07-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turningaccounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turninguser',
            name='nickName',
            field=models.CharField(default='null', max_length=20),
        ),
    ]