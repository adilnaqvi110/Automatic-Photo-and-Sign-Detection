# Generated by Django 3.2.14 on 2022-07-05 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_profile', '0002_auto_20220705_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admit_card',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
        migrations.AlterField(
            model_name='admit_card',
            name='sign_image',
            field=models.ImageField(blank=True, null=True, upload_to='sign_images/'),
        ),
    ]