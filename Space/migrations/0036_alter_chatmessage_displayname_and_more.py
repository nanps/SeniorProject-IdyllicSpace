# Generated by Django 4.0.5 on 2023-04-03 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Space', '0035_remove_spaceroom_id_alter_chatmessage_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='displayName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Space.usermanage'),
        ),
        migrations.AlterField(
            model_name='spaceroom',
            name='roomStatus',
            field=models.CharField(max_length=5),
        ),
    ]
