# Generated by Django 4.0.5 on 2023-04-03 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Space', '0036_alter_chatmessage_displayname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='slug',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]
