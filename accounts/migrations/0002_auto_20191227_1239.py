# Generated by Django 3.0 on 2019-12-27 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='source',
            new_name='user',
        ),
    ]
