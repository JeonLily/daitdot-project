# Generated by Django 2.1.5 on 2019-01-15 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SWUDot', '0006_auto_20190115_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeinfo',
            name='review_count',
            field=models.IntegerField(default='0'),
        ),
    ]
