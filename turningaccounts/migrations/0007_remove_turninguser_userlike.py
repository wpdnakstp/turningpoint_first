# Generated by Django 2.1.8 on 2019-07-31 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turningaccounts', '0006_auto_20190727_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turninguser',
            name='userLike',
        ),
    ]
