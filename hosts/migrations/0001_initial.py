# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-27 15:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50, unique=True, verbose_name='\u4e3b\u673a\u540d')),
                ('ip', models.GenericIPAddressField(unique=True, verbose_name='\u7ba1\u7406IP')),
                ('other_ip', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u5176\u5b83IP')),
                ('asset_type', models.CharField(blank=True, choices=[(b'1', '\u7269\u7406\u673a'), (b'2', '\u865a\u62df\u673a'), (b'3', '\u5bb9\u5668'), (b'4', '\u7f51\u7edc\u8bbe\u5907'), (b'5', '\u5176\u4ed6')], max_length=30, null=True, verbose_name='\u8bbe\u5907\u7c7b\u578b')),
                ('status', models.CharField(blank=True, choices=[(b'1', '\u4f7f\u7528\u4e2d'), (b'2', '\u672a\u4f7f\u7528'), (b'3', '\u6545\u969c'), (b'4', '\u5176\u5b83')], max_length=30, null=True, verbose_name='\u8bbe\u5907\u72b6\u6001')),
                ('os', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf')),
                ('cpu_model', models.CharField(blank=True, max_length=100, null=True, verbose_name='CPU\u578b\u53f7')),
                ('cpu_num', models.CharField(blank=True, max_length=100, null=True, verbose_name='CPU\u6570\u91cf')),
                ('memory', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u5185\u5b58\u5927\u5c0f')),
                ('disk', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u786c\u76d8\u4fe1\u606f')),
                ('memo', models.TextField(blank=True, max_length=200, null=True, verbose_name='\u5907\u6ce8\u4fe1\u606f')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5668',
                'verbose_name_plural': '\u670d\u52a1\u5668\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='\u7ec4\u540d')),
                ('desc', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u63cf\u8ff0')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5668\u7ec4',
                'verbose_name_plural': '\u670d\u52a1\u5668\u7ec4',
            },
        ),
        migrations.CreateModel(
            name='SaltServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.IntegerField(verbose_name='\u7aef\u53e3\u53f7')),
                ('apiurl', models.URLField(blank=True, max_length=20, null=True, verbose_name='salt API\u5730\u5740')),
                ('username', models.CharField(max_length=20, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=50, verbose_name='\u5bc6\u7801')),
                ('ip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hosts.Host', verbose_name='\u670d\u52a1\u5668IP')),
            ],
            options={
                'verbose_name': 'Salt\u670d\u52a1\u5668',
                'verbose_name_plural': 'Salt\u670d\u52a1\u5668\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headImg', models.FileField(upload_to=b'upload/', verbose_name='\u6587\u4ef6\u8def\u5f84')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='\u4e0a\u4f20\u65f6\u95f4')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u6587\u4ef6\u4e0a\u4f20',
                'verbose_name_plural': '\u6587\u4ef6\u4e0a\u4f20',
            },
        ),
        migrations.AddField(
            model_name='host',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hosts.HostGroup', verbose_name='\u8bbe\u5907\u7ec4'),
        ),
    ]
