# Generated by Django 3.2.10 on 2021-12-12 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='img',
            field=models.ImageField(default='images', upload_to='gallery'),
            preserve_default=False,
        ),
    ]