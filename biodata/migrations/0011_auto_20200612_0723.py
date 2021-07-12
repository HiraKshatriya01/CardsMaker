# Generated by Django 3.0.2 on 2020-06-12 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0010_auto_20200612_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='language_name',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='biodata_language_name', to='biodata.LanguageName'),
        ),
    ]
