# Generated by Django 4.2.3 on 2023-09-14 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snap_app', '0002_rename_state_snap_program_name_snapdata_statesnapprogramname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statesnapprogram',
            old_name='name',
            new_name='StateSNAPProgramName',
        ),
    ]
