# Generated by Django 5.0.7 on 2024-07-15 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='orig_id',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='role',
            field=models.CharField(blank=True, choices=[('node', 'Node')], max_length=10, null=True),
        ),
    ]
