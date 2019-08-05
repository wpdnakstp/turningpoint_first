# Generated by Django 2.1.8 on 2019-08-03 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turningaccounts', '0004_auto_20190722_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='turninguser',
            name='userArmyName',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='turninguser',
            name='userBirthDay',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='turninguser',
            name='userGender',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='turninguser',
            name='userId',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='turninguser',
            name='nickName',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='turninguser',
            name='tnPhoneNumb',
            field=models.CharField(max_length=15),
        ),
    ]