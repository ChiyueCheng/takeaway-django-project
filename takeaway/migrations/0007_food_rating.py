# Generated by Django 4.1.7 on 2023-03-11 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("takeaway", "0006_alter_food_discounted_price_alter_food_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="food", name="rating", field=models.IntegerField(default=0),
        ),
    ]
