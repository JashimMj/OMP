# Generated by Django 3.2.5 on 2021-08-02 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0004_specialsupport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialsupport',
            old_name='Titel',
            new_name='Title',
        ),
    ]