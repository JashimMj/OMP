# Generated by Django 3.2.5 on 2021-08-02 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0008_customerfeedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(blank=True, max_length=200, null=True)),
                ('Discription', models.TextField(blank=True, max_length=200, null=True)),
                ('Award_image', models.ImageField(blank=True, null=True, upload_to='icon')),
            ],
        ),
    ]
