# Generated by Django 4.1.1 on 2022-09-29 19:12

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields
import djmoney.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_alter_listing_categoryname_alter_listing_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='startingBid_currency',
            new_name='startingPrice_currency',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='startingBid',
        ),
        migrations.AddField(
            model_name='listing',
            name='startingPrice',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='USD', max_digits=14, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Starting Price'),
        ),
    ]