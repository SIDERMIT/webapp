# Generated by Django 3.0.7 on 2020-06-29 16:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0005_auto_20200629_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='public_id',
            field=models.UUIDField(default=uuid.UUID('d91afef5-8890-42b9-938a-341d99540ec4')),
        ),
    ]
