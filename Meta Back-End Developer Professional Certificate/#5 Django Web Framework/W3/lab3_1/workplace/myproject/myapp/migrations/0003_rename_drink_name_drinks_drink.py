# Generated by Django 5.0.2 on 2024-02-12 11:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_rename_drink_drinks_drink_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="drinks",
            old_name="drink_name",
            new_name="drink",
        ),
    ]