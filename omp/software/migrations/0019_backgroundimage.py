# Generated by Django 3.2.5 on 2021-08-17 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0018_quatation_puser'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='background')),
            ],
        ),
    ]