# Generated by Django 4.2.1 on 2025-01-21 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0037_buyvehicleordermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='buy_vehicle_order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.buyvehicleordermodel', verbose_name='مودل طلب شراء السيارة'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='order_type',
            field=models.CharField(choices=[('buy_car', 'شراء سيارة'), ('car_import', 'استراد السيارة'), ('car_rental', 'ايجار السيارة'), ('car_installment', 'تقسيط السيارة'), ('vehicle_rental_order', 'نقل حمولة'), ('buy_vehicle', 'شراء مركبة')], max_length=20, verbose_name='نوع الطلب'),
        ),
    ]
