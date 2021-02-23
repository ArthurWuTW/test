# Generated by Django 3.0.8 on 2021-02-23 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_id', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('price', models.IntegerField()),
                ('shop_id', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Order',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('stock_pcs', models.IntegerField()),
                ('price', models.IntegerField()),
                ('shop_id', models.CharField(max_length=100)),
                ('vip', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Product',
            },
        ),
    ]
