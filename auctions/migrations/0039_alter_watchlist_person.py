# Generated by Django 4.1.1 on 2022-10-05 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0038_alter_listing_categoryname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userWatchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
