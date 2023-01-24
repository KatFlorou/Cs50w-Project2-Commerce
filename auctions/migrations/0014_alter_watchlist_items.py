# Generated by Django 4.1 on 2022-09-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_rename_category_listing_categoryname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='items',
            field=models.ManyToManyField(blank=True, related_name='watched_listings', to='auctions.listing'),
        ),
    ]