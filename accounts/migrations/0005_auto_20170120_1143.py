# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170120_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='balance_updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='account_id',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name=b'Broker Real account Id '),
        ),
        migrations.AlterField(
            model_name='profile',
            name='account_id2',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name=b'Broker virtual account Id '),
        ),
        migrations.AlterField(
            model_name='profile',
            name='token',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name=b'Broker Real token '),
        ),
        migrations.AlterField(
            model_name='profile',
            name='token2',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name=b'Broker virtual tocken'),
        ),
    ]