# Generated by Django 4.1 on 2024-08-11 17:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_banners"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="img",
            field=models.ImageField(null=True, upload_to="services/"),
        ),
        migrations.AlterField(
            model_name="service",
            name="detail",
            field=models.TextField(),
        ),
    ]
