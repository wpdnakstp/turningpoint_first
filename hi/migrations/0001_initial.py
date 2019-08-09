# Generated by Django 2.1.8 on 2019-08-09 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiaryForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diaryTitle', models.CharField(max_length=200)),
                ('diaryBody', models.TextField()),
                ('diaryDate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
