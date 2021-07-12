# Generated by Django 2.2.19 on 2021-03-06 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0012_businesscard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_name', models.TextField(blank=True, default='{}', null=True)),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Inactive')], default=1)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_languages', to='languages.LanguageName')),
            ],
        ),
    ]