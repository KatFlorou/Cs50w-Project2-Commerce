# Generated by Django 4.1 on 2022-09-26 12:51

from django.db import migrations
import djmoney.models.fields
import djmoney.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_alter_listing_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='categoryname',
        ),
        migrations.AlterField(
            model_name='listing',
            name='startingBid',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='USD', max_digits=14, validators=[djmoney.models.validators.MinMoneyValidator(0)]),
        ),
    ]
