# Generated by Django 5.0.2 on 2024-05-11 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_customer_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="profile_pic",
            field=models.ImageField(blank=True, null=True, upload_to="images"),
        ),
    ]