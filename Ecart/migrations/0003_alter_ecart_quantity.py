# Generated by Django 4.2.5 on 2024-02-24 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecart', '0002_ecart_size_alter_ecart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
