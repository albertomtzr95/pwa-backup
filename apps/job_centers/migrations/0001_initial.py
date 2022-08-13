# Generated by Django 4.1 on 2022-08-06 16:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCenter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('business_name', models.CharField(blank=True, max_length=255, null=True)),
                ('health_manager', models.CharField(blank=True, max_length=255, null=True)),
                ('taxpayer_registration', models.CharField(blank=True, max_length=255, null=True)),
                ('license_number', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=50, null=True)),
                ('web_page', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('messenger', models.CharField(blank=True, max_length=255, null=True)),
                ('sanitary_license', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
