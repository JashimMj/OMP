# Generated by Django 3.2.5 on 2021-08-12 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0017_rename_typeof_insurance_quatation_typeinsurance'),
    ]

    operations = [
        migrations.AddField(
            model_name='quatation',
            name='Puser',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
