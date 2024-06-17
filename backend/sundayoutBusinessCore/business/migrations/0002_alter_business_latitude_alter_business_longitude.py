# Generated by Django 5.0.6 on 2024-06-15 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=8),
        ),
        migrations.AlterField(
            model_name='business',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=8),
        ),
    ]
