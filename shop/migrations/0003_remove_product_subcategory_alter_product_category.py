# Generated by Django 4.2.2 on 2023-07-18 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_category_product_image_product_subcategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Men', 'Men Shoes'), ('Women', 'Women Shoes'), ('Kids', 'Kids Shoes')], max_length=50),
        ),
    ]