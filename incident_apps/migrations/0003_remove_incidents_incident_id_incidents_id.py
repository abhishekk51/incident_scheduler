# Generated by Django 5.0.1 on 2024-01-05 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident_apps', '0002_handler_incidents_delete_tasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incidents',
            name='incident_id',
        ),
        migrations.AddField(
            model_name='incidents',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
