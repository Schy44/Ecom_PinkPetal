# Generated by Django 3.2.9 on 2023-10-25 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SliderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='slider_images/')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(max_length=50)),
                ('image', models.ImageField(upload_to='catagorybag/')),
                ('Category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='petal2.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=30)),
                ('Brand', models.CharField(max_length=50)),
                ('Material', models.CharField(max_length=150)),
                ('Color', models.CharField(max_length=30)),
                ('Item_Weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(max_length=50)),
                ('image', models.ImageField(upload_to='catagorybag/')),
                ('Category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='petal2.category')),
            ],
        ),
    ]
