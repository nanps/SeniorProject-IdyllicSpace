# Generated by Django 4.0.5 on 2023-03-24 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Space', '0022_alter_chatmessage_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='displayName',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
