# Generated by Django 4.1 on 2022-10-04 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_alter_listing_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='status',
            field=models.CharField(choices=[('True', 'Active'), ('False', 'Closed')], default=True, max_length=7),
        ),
    ]
