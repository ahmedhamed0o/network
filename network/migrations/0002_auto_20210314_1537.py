# Generated by Django 3.1.5 on 2021-03-14 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='liked_by',
        ),
    ]
