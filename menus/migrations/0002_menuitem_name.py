# Generated by Django 4.2.6 on 2023-11-01 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='name',
            field=models.CharField(default='Item', max_length=45),
        ),
    ]
