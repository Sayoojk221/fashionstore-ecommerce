# Generated by Django 3.1 on 2020-10-01 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productsize',
            options={'get_latest_by': ['productcolor__colorid']},
        ),
    ]
