# Generated by Django 4.2.5 on 2023-11-20 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='linkedin',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='place',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='postbox',
            field=models.CharField(default='', max_length=255),
        ),
    ]
