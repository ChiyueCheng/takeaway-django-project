# Generated by Django 4.1.7 on 2023-03-11 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("takeaway", "0002_food_wallet_order_comment_basket"),
    ]

    operations = [
        migrations.RemoveField(model_name="userprofile", name="website",),
        migrations.AddField(
            model_name="userprofile",
            name="address",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
