# Generated by Django 5.0.2 on 2024-03-19 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profilepic.png', upload_to='profile_pictures'),
        ),
    ]
