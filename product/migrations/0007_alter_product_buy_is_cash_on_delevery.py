# Generated by Django 4.2.5 on 2024-02-28 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_pro_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_buy',
            name='is_cash_on_delevery',
            field=models.BooleanField(),
        ),
    ]
