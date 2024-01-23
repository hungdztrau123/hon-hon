# Generated by Django 5.0.1 on 2024-01-22 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='ColorVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=100)),
                ('color_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QuantityVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SizeVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('price', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('stock', models.IntegerField(default=100)),
                ('category', models.ForeignKey(choices=[('Vegetables', 'Vegetables'), ('Figures', 'Figures'), ('Computer', 'Computer'), ('Copiers', 'Copiers')], on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('color_type', models.ForeignKey(blank=True, choices=[('Blue', 'Blue'), ('Green', 'Green')], null=True, on_delete=django.db.models.deletion.PROTECT, to='products.colorvariant')),
                ('quantity_type', models.ForeignKey(blank=True, choices=[('Litre', 'Litre'), ('Kilogram', 'Kilogram')], null=True, on_delete=django.db.models.deletion.PROTECT, to='products.quantityvariant')),
                ('size_type', models.ForeignKey(blank=True, choices=[('Big', 'Big'), ('Medium', 'Medium'), ('Small', 'Small')], null=True, on_delete=django.db.models.deletion.PROTECT, to='products.sizevariant')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product')),
            ],
        ),
    ]