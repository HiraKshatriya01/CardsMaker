# Generated by Django 3.0.7 on 2020-06-30 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0009_add_subregion'),
        ('users', '0009_auto_20200618_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='dialcode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.Country'),
        ),
    ]
