# Generated by Django 4.0.5 on 2023-02-22 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Space', '0003_spaceroom_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermanage',
            name='currentSpaceRoom',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
