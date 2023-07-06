# Generated by Django 4.0.5 on 2023-04-09 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Space', '0039_alter_chatmessage_content_alter_chatmessage_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('uid', models.CharField(max_length=1000)),
                ('room_name', models.CharField(max_length=200)),
                ('insession', models.BooleanField(default=True)),
            ],
        ),
    ]