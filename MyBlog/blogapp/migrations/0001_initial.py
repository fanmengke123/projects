# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-29 02:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('cover', models.ImageField(upload_to='static/imgs/banner', verbose_name='封面')),
                ('link_url', models.URLField(max_length=256, verbose_name='链接')),
                ('idx', models.IntegerField(verbose_name='索引')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否被激活')),
            ],
            options={
                'verbose_name_plural': '轮播图',
                'verbose_name': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名字')),
            ],
            options={
                'verbose_name_plural': '分类',
                'verbose_name': '分类',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=256, verbose_name='内容')),
                ('comment_date', models.DateTimeField(verbose_name='评论日期')),
            ],
            options={
                'verbose_name_plural': '评论',
                'verbose_name': '评论',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名字')),
                ('link_url', models.URLField(default='', max_length=256, verbose_name='链接')),
            ],
            options={
                'verbose_name_plural': '友情链接',
                'verbose_name': '友情链接',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('cover', models.ImageField(upload_to='static/imgs/post', verbose_name='封面')),
                ('pub_date', models.DateTimeField(verbose_name='发布日期')),
                ('views', models.IntegerField(default=0, verbose_name='浏览量')),
                ('content', models.TextField(verbose_name='内容')),
                ('recommend', models.BooleanField(default=False, verbose_name='推荐')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.Category', verbose_name='分类')),
            ],
            options={
                'verbose_name_plural': '文章',
                'verbose_name': '文章',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': '标签',
                'verbose_name': '标签',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blogapp.Tags', verbose_name='标签'),
        ),
    ]
