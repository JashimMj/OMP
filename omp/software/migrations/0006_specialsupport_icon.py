# Generated by Django 3.2.5 on 2021-08-02 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0005_rename_titel_specialsupport_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialsupport',
            name='icon',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
