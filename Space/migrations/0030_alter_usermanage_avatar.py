# Generated by Django 4.0.5 on 2023-04-03 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Space', '0029_delete_spaceroommanage_spaceroom_inroom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermanage',
            name='avatar',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
