# Generated by Django 3.2 on 2022-07-05 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220705_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
