# Generated by Django 4.1 on 2022-09-26 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_rename_category_category_categoryname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='category',
            new_name='categoryname',
        ),
    ]