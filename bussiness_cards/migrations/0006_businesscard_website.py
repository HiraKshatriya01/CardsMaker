# Generated by Django 2.2.19 on 2021-03-10 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bussiness_cards', '0005_auto_20210310_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesscard',
            name='website',
            field=models.CharField(default='', max_length=100),
        ),
    ]