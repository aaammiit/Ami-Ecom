# Generated by Django 4.2.5 on 2024-02-24 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecart', '0005_remove_ecart_quantity_remove_ecart_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecart',
            name='size',
            field=models.CharField(default='M', max_length=100),
        ),
    ]
