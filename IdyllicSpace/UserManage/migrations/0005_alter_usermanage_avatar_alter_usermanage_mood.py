# Generated by Django 4.0.5 on 2023-01-15 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManage', '0004_remove_usermanage_id_alter_usermanage_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermanage',
            name='avatar',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='usermanage',
            name='mood',
            field=models.CharField(max_length=30, null=True),
        ),
    ]