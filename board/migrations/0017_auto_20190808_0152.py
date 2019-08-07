# Generated by Django 2.1.8 on 2019-08-08 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0016_auto_20190803_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developcomment',
            name='develop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dcomments', to='board.Develop'),
        ),
        migrations.AlterField(
            model_name='noticecomment',
            name='notice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ncomments', to='board.Notice'),
        ),
    ]
