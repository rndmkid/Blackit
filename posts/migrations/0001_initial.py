# Generated by Django 2.1 on 2018-11-30 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('subreddits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
                ('isComment', models.BooleanField(default=False)),
                ('title', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.User')),
                ('response_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='posts.Post')),
                ('subreddit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='subreddits.Subreddit')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(choices=[(1, 'up'), (-1, 'down')])),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.User')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
            ],
        ),
    ]
