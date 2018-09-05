# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-05 18:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badgeuser', '0026_auto_20180817_0913'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='badgeuser',
            options={'permissions': (('view_issuer_tab', 'User can view Issuer tab in front end'), ('has_faculty_scope', 'User has faculty scope'), ('has_institution_scope', 'User has institution scope')), 'verbose_name': 'badge user', 'verbose_name_plural': 'badge users'},
        ),
    ]
