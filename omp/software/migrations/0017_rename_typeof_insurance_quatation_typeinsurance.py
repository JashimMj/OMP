# Generated by Django 3.2.5 on 2021-08-11 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0016_alter_quatation_stadate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quatation',
            old_name='TypeOf_Insurance',
            new_name='TypeInsurance',
        ),
    ]
