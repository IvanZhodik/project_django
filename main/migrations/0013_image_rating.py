# Generated by Django 4.1.4 on 2023-01-30 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_image_rating_remove_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='rating',
            field=models.IntegerField(db_index=True, max_length=200, null=True, unique=True),
        ),
    ]
