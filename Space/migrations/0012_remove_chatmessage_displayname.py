# Generated by Django 4.0.5 on 2023-03-22 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Space', '0011_rename_message_chatmessage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='displayName',
        ),
    ]
