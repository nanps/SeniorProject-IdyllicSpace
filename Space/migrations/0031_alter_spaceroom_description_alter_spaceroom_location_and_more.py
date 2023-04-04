# Generated by Django 4.0.5 on 2023-04-03 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Space', '0030_alter_usermanage_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spaceroom',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spaceroom',
            name='location',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='usermanage',
            name='currentSpaceRoom',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
