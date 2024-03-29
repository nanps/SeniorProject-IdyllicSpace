# Generated by Django 4.0.5 on 2023-04-03 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Space', '0034_alter_spaceroom_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spaceroom',
            name='id',
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='slug',
            field=models.CharField(max_length=25, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='spaceroom',
            name='capacity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='spaceroom',
            name='location',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='spaceroom',
            name='slug',
            field=models.SlugField(primary_key=True, serialize=False, unique=True),
        ),
    ]
