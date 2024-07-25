# Generated by Django 5.0.7 on 2024-07-15 03:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('domain', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'wp_websites',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('status', models.CharField(default='0', max_length=10)),
                ('role', models.CharField(blank=True, max_length=10, null=True)),
                ('level', models.IntegerField(blank=True, null=True)),
                ('google_path', models.TextField(blank=True, null=True)),
                ('orig_path', models.TextField(blank=True, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='scraper.category')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper.website')),
            ],
            options={
                'db_table': 'wp_categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('specification', models.TextField(blank=True, null=True)),
                ('features', models.TextField(blank=True, null=True)),
                ('images', models.TextField(blank=True, null=True)),
                ('orig_id', models.CharField(blank=True, max_length=30, null=True)),
                ('wwmall_id', models.BigIntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('sku', models.CharField(blank=True, max_length=100, null=True)),
                ('sale_price', models.FloatField(blank=True, null=True)),
                ('regular_price', models.FloatField(blank=True, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('attributes', models.TextField(blank=True, null=True)),
                ('variants', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper.category')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper.website')),
            ],
            options={
                'db_table': 'wp_products',
            },
        ),
    ]
