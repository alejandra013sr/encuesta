# Generated by Django 3.2.4 on 2021-07-03 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0002_alter_userprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=255, null=True, unique=True),
        ),
    ]