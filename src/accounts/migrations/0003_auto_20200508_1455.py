# Generated by Django 3.0.6 on 2020-05-08 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170803_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, default='img/default.png', height_field='height_field', null=True, upload_to='', verbose_name='profile picture', width_field='width_field'),
        ),
    ]
