# Generated by Django 4.2.11 on 2024-04-18 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_updaetd_at_comment_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Post',
            new_name='post',
        ),
    ]
