# Generated by Django 2.1.5 on 2019-01-16 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SWUDot', '0009_auto_20190115_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeinfo',
            name='st_image',
            field=models.ImageField(default='no_image.png', upload_to=''),
        ),
    ]
