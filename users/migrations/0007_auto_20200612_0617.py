# Generated by Django 3.0.2 on 2020-06-12 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200612_0616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='user',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='user_id',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]