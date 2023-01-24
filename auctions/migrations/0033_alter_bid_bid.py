# Generated by Django 4.1.1 on 2022-10-05 09:12

from django.db import migrations
import djmoney.models.fields
import djmoney.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0032_bid_bid_currency_alter_bid_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='USD', max_digits=14, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name=''),
        ),
    ]
