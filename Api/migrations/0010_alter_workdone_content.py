# Generated by Django 4.1.2 on 2023-10-24 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0009_remove_workdone_brand_remove_workdone_image_display_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workdone',
            name='content',
            field=models.CharField(max_length=10000),
        ),
    ]
