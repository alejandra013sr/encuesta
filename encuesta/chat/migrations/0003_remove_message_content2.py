# Generated by Django 3.0.7 on 2022-01-12 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_message_content2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='content2',
        ),
    ]
