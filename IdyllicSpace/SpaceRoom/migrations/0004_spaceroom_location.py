# Generated by Django 4.0.5 on 2022-12-22 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpaceRoom', '0003_spaceroom_description_alter_spaceroom_roomname'),
    ]

    operations = [
        migrations.AddField(
            model_name='spaceroom',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
