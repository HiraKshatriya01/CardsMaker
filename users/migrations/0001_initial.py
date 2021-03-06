# Generated by Django 3.0.2 on 2020-02-03 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdsToShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ads_name', models.CharField(default='', max_length=100)),
                ('ads_type', models.CharField(default='', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('user_mobile', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('ads_watched', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('active', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Inactive')], default=1)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransferToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_amount', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('reciever_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever_user_details', to='users.UserDetails')),
                ('sender_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_user_details', to='users.UserDetails')),
            ],
        ),
        migrations.CreateModel(
            name='TokenTransactionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('cm_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_transaction_details', to='users.UserDetails')),
            ],
        ),
        migrations.CreateModel(
            name='MoneyPaymentHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('cm_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_payment_details', to='users.UserDetails')),
            ],
        ),
        migrations.CreateModel(
            name='AdsWatched',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('earned_token', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('ads_watched', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads_watched_by_user', to='users.AdsToShow')),
                ('cm_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads_watched_user', to='users.UserDetails')),
            ],
        ),
        migrations.CreateModel(
            name='AccountBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_balance', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('balance', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('cm_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_account_details', to='users.UserDetails')),
            ],
        ),
    ]
