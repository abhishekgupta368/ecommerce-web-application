# Generated by Django 3.1.1 on 2020-09-26 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_cart_cartitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='card_id',
            new_name='cart_id',
        ),
    ]