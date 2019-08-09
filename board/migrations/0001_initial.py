# Generated by Django 2.1.8 on 2019-08-09 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Develop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
                ('postHit', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Developcomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentdate', models.DateTimeField(auto_now=True, null=True)),
                ('commentbody', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Free',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
                ('postHit', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Freecomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentdate', models.DateTimeField(auto_now=True, null=True)),
                ('commentbody', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
                ('postHit', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Noticecomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentdate', models.DateTimeField(auto_now=True, null=True)),
                ('commentbody', models.TextField()),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='board.Notice')),
            ],
        ),
    ]
