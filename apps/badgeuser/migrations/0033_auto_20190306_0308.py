# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-06 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badgeuser', '0032_auto_20190304_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='termsversion',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='termsversion',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='termsversion',
            name='terms_and_conditions_template',
            field=models.CharField(max_length=512, null=True, verbose_name='Terms and conditions template'),
        ),
    ]
