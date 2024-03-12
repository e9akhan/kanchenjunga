"""
    Module name :- 0003_alter_allocation_slug
"""


# Generated by Django 4.2.9 on 2024-03-12 11:37

from django.db import migrations, models


class Migration(migrations.Migration):
    """
        Migration class.
    """

    dependencies = [
        ("store", "0002_alter_allocation_release_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="allocation",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]