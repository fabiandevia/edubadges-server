# Generated by Django 2.2.14 on 2021-02-18 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuer', '0080_auto_20210218_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuer',
            old_name='name',
            new_name='name_english',
        ),
        migrations.AddField(
            model_name='issuer',
            name='name_dutch',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
