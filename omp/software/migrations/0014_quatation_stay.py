# Generated by Django 3.2.5 on 2021-08-11 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0013_quatation'),
    ]

    operations = [
        migrations.AddField(
            model_name='quatation',
            name='stay',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
    ]
