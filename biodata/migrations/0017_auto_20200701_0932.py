# Generated by Django 3.0.7 on 2020-07-01 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0016_auto_20200627_0545'),
    ]

    operations = [
        migrations.AddField(
            model_name='labelname',
            name='completion_year',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='labelname',
            name='diet',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
