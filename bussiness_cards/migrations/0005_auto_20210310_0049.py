# Generated by Django 2.2.19 on 2021-03-10 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bussiness_cards', '0004_auto_20210308_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesscard',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='label_language_name', to='languages.Business'),
        ),
    ]