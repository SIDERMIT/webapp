# Generated by Django 3.1 on 2020-10-05 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0020_transportnetwork_optimization_error_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optimizationresultperroute',
            name='transport_network',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.transportnetwork'),
        ),
    ]
