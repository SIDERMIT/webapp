# Generated by Django 3.0.7 on 2020-06-28 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='optimization',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='passenger',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='scene',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='transportmode',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='transportnetwork',
            old_name='create_at',
            new_name='created_at',
        ),
    ]