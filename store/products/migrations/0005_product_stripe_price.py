# Generated by Django 4.1.1 on 2022-12-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_options_alter_productcategory_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stripe_price',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
