# Generated by Django 4.2.1 on 2023-05-04 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submission_link',
            field=models.URLField(),
        ),
    ]
