# Generated by Django 2.1.5 on 2019-01-18 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SWUDot', '0018_schooladressbook'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storeinfo',
            options={'ordering': ['-st_score']},
        ),
    ]
