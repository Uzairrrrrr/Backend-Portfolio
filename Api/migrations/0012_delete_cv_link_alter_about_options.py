# Generated by Django 4.1.2 on 2023-10-27 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0011_alter_testimonials_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CV_link',
        ),
        migrations.AlterModelOptions(
            name='about',
            options={},
        ),
    ]
