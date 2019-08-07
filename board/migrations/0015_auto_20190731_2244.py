# Generated by Django 2.1.8 on 2019-07-31 22:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0014_merge_20190731_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developcomment',
            name='tnDevelopCommentUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='freecomment',
            name='tnFreeCommentUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]