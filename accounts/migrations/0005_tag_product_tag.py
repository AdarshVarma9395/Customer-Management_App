# Generated by Django 5.0.2 on 2024-03-28 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_order_customer_order_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="tag",
            field=models.ManyToManyField(to="accounts.tag"),
        ),
    ]
