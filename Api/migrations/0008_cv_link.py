# Generated by Django 4.1.2 on 2023-10-24 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0007_rename_project_url_workdone_project_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='CV_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
