# Generated by Django 4.1.1 on 2022-09-23 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_listing_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='items',
            field=models.ManyToManyField(blank=True, to='auctions.listing'),
        ),
    ]