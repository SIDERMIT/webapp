# Generated by Django 3.1 on 2020-10-02 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0015_auto_20201002_0749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='optimizationresult',
            name='optimization',
        ),
        migrations.RemoveField(
            model_name='optimizationresultpermode',
            name='optimization',
        ),
        migrations.RemoveField(
            model_name='optimizationresultperroute',
            name='optimization',
        ),
        migrations.AddField(
            model_name='optimizationresult',
            name='transport_network',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='storage.transportnetwork'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='optimizationresultpermode',
            name='transport_network',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='storage.transportnetwork'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='optimizationresultperroute',
            name='transport_network',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='storage.transportnetwork'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transportnetwork',
            name='optimization_status',
            field=models.CharField(choices=[('queued', 'Queued'), ('processing', 'Processing'), ('finished', 'Finished'), ('error', 'Error')], default='queued', max_length=20),
        ),
        migrations.DeleteModel(
            name='Optimization',
        ),
    ]