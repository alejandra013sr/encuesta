# Generated by Django 3.2.6 on 2021-08-17 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagenes', '0003_auto_20210814_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likeimage',
            name='cant_likes',
            field=models.IntegerField(default=0),
        ),
    ]