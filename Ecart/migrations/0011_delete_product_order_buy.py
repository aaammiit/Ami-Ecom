# Generated by Django 4.2.5 on 2024-02-25 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecart', '0010_remove_product_order_buy_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product_order_buy',
        ),
    ]
