# Generated by Django 4.2.1 on 2023-07-08 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fun', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
