# Generated by Django 4.1.4 on 2023-02-04 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_image_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
    ]