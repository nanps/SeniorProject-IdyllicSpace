# Generated by Django 4.0.5 on 2023-03-22 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Space', '0012_remove_chatmessage_displayname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
