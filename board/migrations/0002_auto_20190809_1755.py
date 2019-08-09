<<<<<<< HEAD:board/migrations/0002_auto_20190809_1720.py
# Generated by Django 2.1.8 on 2019-08-09 17:20
=======
# Generated by Django 2.1.8 on 2019-08-09 17:55
>>>>>>> fc3edda615d296f711ff1becaeedb246d6eb26e1:board/migrations/0002_auto_20190809_1755.py

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
<<<<<<< HEAD:board/migrations/0002_auto_20190809_1720.py
            model_name='noticecomment',
            name='noticeCommentUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
=======
            model_name='develop',
            name='postHit',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='develop',
            name='tnUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tnDevelopUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='develop',
            name='userLikeName',
            field=models.ManyToManyField(related_name='dlikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='developcomment',
            name='tnDevelopCommentUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='free',
            name='postHit',
            field=models.PositiveIntegerField(default=0),
>>>>>>> fc3edda615d296f711ff1becaeedb246d6eb26e1:board/migrations/0002_auto_20190809_1755.py
        ),
        migrations.AddField(
            model_name='free',
            name='tnUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tnFreeUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='free',
            name='userLikeName',
            field=models.ManyToManyField(related_name='flikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='freecomment',
            name='tnFreeCommentUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notice',
            name='tnUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='turningUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notice',
<<<<<<< HEAD:board/migrations/0002_auto_20190809_1720.py
            name='userLikeName',
            field=models.ManyToManyField(related_name='nlikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='freecomment',
            name='free',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='board.Free'),
        ),
        migrations.AddField(
            model_name='freecomment',
            name='tnFreeCommentUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='free',
            name='tnUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tnFreeUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='free',
=======
            name='tnUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='turningUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notice',
>>>>>>> fc3edda615d296f711ff1becaeedb246d6eb26e1:board/migrations/0002_auto_20190809_1755.py
            name='userLikeName',
            field=models.ManyToManyField(related_name='nlikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
<<<<<<< HEAD:board/migrations/0002_auto_20190809_1720.py
            model_name='developcomment',
            name='develop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='board.Develop'),
        ),
        migrations.AddField(
            model_name='developcomment',
            name='tnDevelopCommentUser',
=======
            model_name='noticecomment',
            name='noticeCommentUser',
>>>>>>> fc3edda615d296f711ff1becaeedb246d6eb26e1:board/migrations/0002_auto_20190809_1755.py
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='develop',
            name='tnUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tnDevelopUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='develop',
            name='userLikeName',
            field=models.ManyToManyField(related_name='dlikes', to=settings.AUTH_USER_MODEL),
        ),
    ]