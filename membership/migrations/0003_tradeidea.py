# Generated by Django 4.0.6 on 2022-07-08 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_alter_reservation_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tradeidea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pair', models.CharField(choices=[('NAS100', 'NAS100'), ('US30', 'US30'), ('GOLD', 'GOLD'), ('USDJPY', 'USDJPY'), ('GBPJPY', 'GBPJPY'), ('GBPUSD', 'GBPUSD'), ('CADCHF', 'CADCHF'), ('NZDUSD', 'NZDUSD'), ('EURJPY', 'EURJPY'), ('EURUSD', 'EURUSD'), ('USDCAD', 'USDCAD'), ('BTCUSD', 'BTCUSD'), ('CHFJPY', 'CHFJPY'), ('EURGBP', 'EURGBP'), ('AUDUSD', 'AUDUSD'), ('USDCHF', 'USDCHF')], default='NAS100', max_length=20)),
                ('chart', models.CharField(choices=[('GLOBALPRIME', 'GLOBALPRIME'), ('FXCM', 'FXCM'), ('CURREBCYCOM', 'CURREBCYCOM'), ('OANDA', 'OANDA'), ('SAXO', 'SAXO')], default='GLOBALPRIME', max_length=50)),
                ('entry', models.CharField(default='0.00000', max_length=20)),
                ('tp1', models.CharField(default='0.00000', max_length=20)),
                ('tp2', models.CharField(blank=True, default='0.00000', max_length=20, null=True)),
                ('tp3', models.CharField(blank=True, default='0.00000', max_length=20, null=True)),
                ('sl', models.CharField(default='0.00000', max_length=20)),
            ],
        ),
    ]
