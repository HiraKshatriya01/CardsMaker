# Generated by Django 3.0.2 on 2020-06-12 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200612_0615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='user_id',
            new_name='user',
        ),
    ]
