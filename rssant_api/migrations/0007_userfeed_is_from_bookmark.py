# Generated by Django 2.1.7 on 2019-04-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rssant_api', '0006_auto_20190418_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfeed',
            name='is_from_bookmark',
            field=models.BooleanField(blank=True, default=False, help_text='是否从书签导入', null=True),
        ),
    ]
