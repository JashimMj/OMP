# Generated by Django 3.2.5 on 2021-08-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0022_auto_20210817_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='Coustomer_Year_End',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='rate',
            name='Coustomer_Year_Start',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='rate',
            name='Gross',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='rate',
            name='Stay_Days_End',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='rate',
            name='Stay_Days_Start',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='rate',
            name='Vat',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='rate',
            name='net',
            field=models.IntegerField(default=True),
        ),
    ]