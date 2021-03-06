# Generated by Django 3.2.6 on 2021-08-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0002_coin_market_cap'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='price_change_percentage_24h',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='coin',
            name='total_volume',
            field=models.BigIntegerField(blank=True, default=0),
        ),
    ]
