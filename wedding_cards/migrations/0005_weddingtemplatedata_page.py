# Generated by Django 2.2.3 on 2021-02-14 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_cards', '0004_auto_20210214_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='weddingtemplatedata',
            name='page',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
