# Generated by Django 2.1.8 on 2019-07-27 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turningaccounts', '0004_auto_20190722_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='turninguser',
            name='likeUser',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
