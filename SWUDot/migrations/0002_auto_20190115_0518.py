# Generated by Django 2.1.5 on 2019-01-15 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SWUDot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='st_name',
        ),
        migrations.AddField(
            model_name='review',
            name='store',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='rev', to='SWUDot.StoreInfo'),
        ),
    ]