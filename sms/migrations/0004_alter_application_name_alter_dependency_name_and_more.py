# Generated by Django 4.2.15 on 2024-08-18 23:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_alter_application_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='dependency',
            name='name',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='deploymenttool',
            name='name',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='environmentvariable',
            name='name',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='monitoringtool',
            name='name',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='port',
            name='port_number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1024), django.core.validators.MaxValueValidator(65535)]),
        ),
        migrations.AlterField(
            model_name='servicesystem',
            name='ip_address',
            field=models.GenericIPAddressField(unpack_ipv4=True),
        ),
        migrations.AlterField(
            model_name='servicesystem',
            name='name',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
    ]
