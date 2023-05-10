# Generated by Django 4.1.5 on 2023-04-22 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Space', '0042_roommember'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='update_time',
            field=models.DateTimeField(auto_now=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='content',
            field=models.TextField(),
        ),
    ]
