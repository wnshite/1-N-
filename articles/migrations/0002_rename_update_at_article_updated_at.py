# Generated by Django 5.1.7 on 2025-03-24 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
