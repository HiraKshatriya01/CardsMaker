# Generated by Django 2.2.19 on 2021-03-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latter_had', '0008_auto_20210328_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='latterhadcard',
            name='website',
            field=models.CharField(default='', max_length=100),
        ),
    ]