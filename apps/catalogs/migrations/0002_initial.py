# Generated by Django 4.1 on 2022-08-06 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogs', '0001_initial'),
        ('job_centers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessactivity',
            name='job_center',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter'),
        ),
        migrations.AddField(
            model_name='applicationmethod',
            name='job_center',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter'),
        ),
    ]