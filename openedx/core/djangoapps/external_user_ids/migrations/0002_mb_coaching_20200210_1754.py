# Generated by Django 1.11.28 on 2020-02-10 17:54


from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('external_user_ids', '0001_initial'),
    ]

    coaching_name = 'mb_coaching'

    def create_mb_coaching_type(apps, schema_editor):
        """
        Add a MicroBachelors (MB) coaching type
        """
        ExternalIdType = apps.get_model('external_user_ids', 'ExternalIdType')
        ExternalIdType.objects.update_or_create(name=Migration.coaching_name, description='MicroBachelors Coaching')

    def delete_mb_coaching_type(apps, schema_editor):
        """
        Delete the MicroBachelors (MB) coaching type
        """
        ExternalIdType = apps.get_model('external_user_ids', 'ExternalIdType')
        ExternalIdType.objects.filter(
            name=Migration.coaching_name
        ).delete()

    operations = [
        migrations.RunPython(create_mb_coaching_type, reverse_code=delete_mb_coaching_type),
    ]
