# Generated by Django 4.0.1 on 2022-01-24 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]