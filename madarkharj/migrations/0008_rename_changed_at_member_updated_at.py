# Generated by Django 5.1.1 on 2024-09-14 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madarkharj', '0007_member_changed_at_member_joined_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='changed_at',
            new_name='updated_at',
        ),
    ]
