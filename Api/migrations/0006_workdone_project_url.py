# Generated by Django 4.1.2 on 2023-10-24 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0005_alter_education_date_alter_work_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='workdone',
            name='Project_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
