# Generated by Django 4.1.2 on 2022-10-12 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_time', models.DateTimeField(auto_now_add=True, verbose_name='Upload Time')),
                ('last_edit_time', models.DateTimeField(auto_now=True, verbose_name='Last Edit Time')),
                ('image_file', models.ImageField(max_length=300, upload_to='img/%Y%m/%d/', verbose_name='File')),
            ],
        ),
    ]
