# Generated by Django 4.1.7 on 2023-03-17 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_wishlist_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', unique=True),
        ),
    ]