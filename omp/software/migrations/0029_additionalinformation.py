# Generated by Django 3.2.5 on 2021-08-19 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0028_alter_rate_coustomer_year_start'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInformation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Address', models.CharField(blank=True, max_length=555, null=True)),
                ('Additioninfo', models.CharField(blank=True, max_length=555, null=True)),
                ('DAddress', models.CharField(blank=True, max_length=555, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.CharField(blank=True, max_length=50, null=True)),
                ('NID', models.CharField(blank=True, max_length=50, null=True)),
                ('pasport', models.ImageField(blank=True, null=True, upload_to='passport')),
                ('quatation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='software.quatation')),
            ],
        ),
    ]
