# Generated by Django 2.2.20 on 2021-05-05 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xblock_config', '0002_courseeditltifieldsenabledflag'),
    ]

    operations = [
        # Since this model only needs to be moved, we just want to
        # indicate to Django that the model is no longer here without
        # actually deleting any data from the database.
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.DeleteModel('CourseEditLTIFieldsEnabledFlag')
            ],
        )
    ]
