# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-20 19:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sappsapp', '0002_auto_20180120_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('disc', models.CharField(max_length=200)),
                ('video', models.FileField(upload_to='documents/video/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='assignments',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='assignments',
            name='image',
        ),
        migrations.RemoveField(
            model_name='assignments',
            name='location',
        ),
        migrations.RemoveField(
            model_name='univresults',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='univresults',
            name='image',
        ),
        migrations.RemoveField(
            model_name='univresults',
            name='location',
        ),
        migrations.AddField(
            model_name='assignments',
            name='disc',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assignments',
            name='fil',
            field=models.FileField(default='', upload_to='documents/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assignments',
            name='topic',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='univresults',
            name='intern1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='univresults',
            name='intern1max',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='univresults',
            name='mark1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='univresults',
            name='max1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='univresults',
            name='res1',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='univresults',
            name='semid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='univresults',
            name='sub1',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='univresults',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='univresults',
            name='total1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='assignments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
