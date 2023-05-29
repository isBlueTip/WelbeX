# Generated by Django 4.2.1 on 2023-05-29 12:17

from django.db import migrations, models
import django.db.models.deletion
import trucks.validators.payload_capacity_validator
import trucks.validators.truck_number_validator


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("locations", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Truck",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "unique_number",
                    models.CharField(
                        blank=True,
                        max_length=5,
                        unique=True,
                        validators=[trucks.validators.truck_number_validator.validate_unique_truck_number],
                        verbose_name="Truck number",
                    ),
                ),
                (
                    "payload_capacity",
                    models.PositiveIntegerField(
                        validators=[trucks.validators.payload_capacity_validator.validate_payload_capacity],
                        verbose_name="Max cargo weight carried by the truck",
                    ),
                ),
                (
                    "current_location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="trucks", to="locations.location"
                    ),
                ),
            ],
        ),
    ]
