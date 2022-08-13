# Generated by Django 4.1 on 2022-08-06 17:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('job_centers', '0001_initial'),
        ('catalogs', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indication',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('key', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Plague',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlagueCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('key', models.CharField(max_length=255)),
                ('hierarchy', models.PositiveSmallIntegerField()),
                ('cost', models.FloatField()),
                ('min_cost', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogs.plaguecategory')),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UnitProduct',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TypeProduct',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('value', models.SmallIntegerField(default=16)),
                ('is_main', models.BooleanField(default=False)),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('key_string', models.CharField(max_length=100)),
                ('module', models.CharField(choices=[('CO', 'Companies'), ('CU', 'Customers'), ('EM', 'Employees'), ('QO', 'Quotes'), ('EV', 'Events')], default='CO', max_length=2)),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('frequency_days', models.PositiveSmallIntegerField(default=0)),
                ('certificate_expiration_days', models.PositiveSmallIntegerField(default=0)),
                ('follow_up_days', models.PositiveSmallIntegerField(default=0)),
                ('disinfection', models.BooleanField(default=False)),
                ('show_price', models.BooleanField(default=True)),
                ('cover', models.CharField(blank=True, max_length=255, null=True)),
                ('indication_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogs.indication')),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RejectionReason',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PriceListPlague',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
                ('plague', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogs.plague')),
                ('price_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogs.pricelist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='pricelist',
            name='service_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogs.servicetype'),
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='plague',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogs.plaguecategory'),
        ),
        migrations.AddField(
            model_name='plague',
            name='job_center',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter'),
        ),
        migrations.CreateModel(
            name='PaymentWay',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('credit_days', models.PositiveSmallIntegerField(default=0)),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OriginSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InfestationDegree',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('percentage', models.SmallIntegerField()),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomDescription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('EX', 'Gasto'), ('OR', 'Orden de Compra')], default='EX', max_length=2)),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cleaning',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CancellationReason',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('job_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_centers.jobcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
