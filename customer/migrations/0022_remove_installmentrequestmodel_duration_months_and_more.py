# Generated by Django 4.2.1 on 2025-01-12 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0021_remove_installmentrequestmodel_customer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='installmentrequestmodel',
            name='duration_months',
        ),
        migrations.RemoveField(
            model_name='installmentrequestmodel',
            name='monthly_installment',
        ),
    ]
