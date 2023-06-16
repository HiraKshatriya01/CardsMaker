# Generated by Django 4.1.5 on 2023-03-11 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_payment_payment_status_alter_payment_status'),
        ('bussiness_cards', '0011_auto_20210517_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesscard',
            name='paid_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bussiness_cards.businesstemplatedata'),
        ),
        migrations.AddField(
            model_name='businesscard',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.payment'),
        ),
    ]