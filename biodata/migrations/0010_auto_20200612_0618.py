# Generated by Django 3.0.2 on 2020-06-12 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0009_auto_20200204_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='biodata_status',
            field=models.IntegerField(choices=[(1, 'DRAFT'), (2, 'PUCHASED'), (3, 'WATCHED_ADS'), (4, 'DELETED')], default=1),
        ),
    ]
