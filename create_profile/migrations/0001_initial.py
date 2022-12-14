# Generated by Django 3.2.14 on 2022-07-05 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admit_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('profile_image', models.ImageField(upload_to='')),
                ('sign_image', models.ImageField(upload_to='')),
                ('date_of_birth', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
            ],
        ),
    ]
