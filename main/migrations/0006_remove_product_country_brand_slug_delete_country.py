# Generated by Django 4.1.4 on 2023-01-26 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_country_brand_image_alter_brand_name_product_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='country',
        ),
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]