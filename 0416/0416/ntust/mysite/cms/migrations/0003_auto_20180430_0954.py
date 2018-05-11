# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-30 01:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20180427_0112'),
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='Bookshops',
            new_name='Myself',
        ),
        migrations.RemoveField(
            model_name='books',
            name='bookshop',
        ),
        migrations.DeleteModel(
            name='Books',
        ),
        migrations.AddField(
            model_name='member',
            name='myself',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Myself'),
        ),
    ]
