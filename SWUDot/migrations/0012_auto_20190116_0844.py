# Generated by Django 2.1.5 on 2019-01-16 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SWUDot', '0011_auto_20190116_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_image',
            field=models.ImageField(default='no_image.png', upload_to='reviewImages/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.ImageField(default='no_image.png', upload_to='userImages/%Y/%m/%d'),
        ),
    ]
