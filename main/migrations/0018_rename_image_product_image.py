# Generated by Django 4.1.4 on 2023-02-04 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_product_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Product_image',
        ),
    ]
