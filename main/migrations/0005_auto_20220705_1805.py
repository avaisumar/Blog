# Generated by Django 3.2 on 2022-07-05 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]