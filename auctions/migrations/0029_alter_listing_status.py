# Generated by Django 4.1.1 on 2022-10-05 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0028_alter_listing_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='status',
            field=models.BooleanField(),
        ),
    ]
