# Generated by Django 4.2.1 on 2025-01-06 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_carimportmodel_shippingcompanymodel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carimportmodel',
            name='shipping_cost',
        ),
        migrations.AddField(
            model_name='carimportmodel',
            name='exterior_color',
            field=models.CharField(choices=[('white', 'أبيض'), ('black', 'أسود'), ('silver', 'فضي'), ('gray', 'رمادي'), ('blue', 'أزرق'), ('red', 'أحمر'), ('green', 'أخضر'), ('yellow', 'أصفر'), ('brown', 'بني'), ('beige', 'بيج'), ('orange', 'برتقالي'), ('gold', 'ذهبي'), ('purple', 'بنفسجي'), ('pink', 'وردي')], help_text='اختر اللون الخارجي للسيارة.', max_length=20, null=True, verbose_name='اللون الخارجي'),
        ),
        migrations.AddField(
            model_name='carimportmodel',
            name='icon',
            field=models.ImageField(blank=True, help_text='اختر صورة الرئيسية التي ستظهر للسيارة (اختياري).', null=True, upload_to='car_icons/', verbose_name='الصورة الرئيسية'),
        ),
        migrations.AddField(
            model_name='carimportmodel',
            name='interior_color',
            field=models.CharField(choices=[('beige', 'بيج'), ('black', 'أسود'), ('gray', 'رمادي'), ('brown', 'بني'), ('white', 'أبيض'), ('red', 'أحمر'), ('blue', 'أزرق'), ('tan', 'لون الجلد الطبيعي'), ('ivory', 'عاجي'), ('chocolate', 'شوكولاتي'), ('dark_gray', 'رمادي غامق'), ('light_gray', 'رمادي فاتح'), ('cream', 'كريمي'), ('orange', 'برتقالي'), ('green', 'أخضر'), ('purple', 'بنفسجي'), ('custom', 'اخرى')], help_text='اختر اللون الداخلي للسيارة.', max_length=20, null=True, verbose_name='اللون الداخلي'),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='year',
            field=models.PositiveIntegerField(help_text='أدخل سنة الصنع السيارة.', null=True, verbose_name='سنة الصنع'),
        ),
        migrations.AlterField(
            model_name='carimportmodel',
            name='brand',
            field=models.CharField(choices=[('toyota', 'تويوتا'), ('nissan', 'نيسان'), ('honda', 'هوندا'), ('bmw', 'بي إم دبليو'), ('mercedes', 'مرسيدس'), ('audi', 'أودي'), ('chevrolet', 'شيفروليه'), ('hyundai', 'هيونداي'), ('kia', 'كيا'), ('ford', 'فورد'), ('volkswagen', 'فولكس واجن'), ('peugeot', 'بيجو'), ('renault', 'رينو'), ('mazda', 'مازدا'), ('suzuki', 'سوزوكي'), ('volvo', 'فولفو'), ('porsche', 'بورش'), ('land_rover', 'لاند روفر'), ('jaguar', 'جاجوار'), ('tesla', 'تسلا'), ('mitsubishi', 'ميتسوبيشي'), ('subaru', 'سوبارو'), ('gmc', 'جي إم سي'), ('cadillac', 'كاديلاك'), ('lincoln', 'لينكولن'), ('chrysler', 'كرايسلر'), ('dodge', 'دودج'), ('jeep', 'جيب'), ('fiat', 'فيات'), ('alfa_romeo', 'ألفا روميو'), ('ferrari', 'فيراري'), ('lamborghini', 'لامبورجيني'), ('aston_martin', 'أستون مارتن'), ('bentley', 'بنتلي'), ('rolls_royce', 'رولز رويس'), ('maserati', 'مازيراتي'), ('bugatti', 'بوجاتي'), ('infiniti', 'إنفينيتي'), ('lexus', 'لكزس'), ('acura', 'أكيورا'), ('saab', 'ساب'), ('skoda', 'سكودا'), ('seat', 'سيات'), ('opel', 'أوبل'), ('citroen', 'ستروين'), ('geely', 'جيلي'), ('mg', 'إم جي'), ('chery', 'شيري'), ('great_wall', 'جريت وول'), ('byd', 'بي واي دي'), ('jac', 'جاك'), ('haval', 'هافال'), ('baic', 'بايك'), ('zotye', 'زوتي'), ('ssangyong', 'سانغ يونغ')], help_text='اختر ماركة السيارة من الخيارات المتاحة.', max_length=20, verbose_name='الماركة'),
        ),
        migrations.AlterField(
            model_name='carimportmodel',
            name='condition',
            field=models.CharField(choices=[('new', 'جديدة'), ('used', 'مستعملة')], help_text='اختر حالة السيارة (جديدة، مستعملة، إلخ).', max_length=10, null=True, verbose_name='الحالة'),
        ),
        migrations.AlterField(
            model_name='carimportmodel',
            name='model',
            field=models.CharField(help_text='أدخل موديل السيارة بشكل دقيق.', max_length=50, verbose_name='موديل السيارة'),
        ),
        migrations.AlterField(
            model_name='carimportmodel',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='سعر السيارة'),
        ),
        migrations.AlterField(
            model_name='carimportmodel',
            name='year',
            field=models.PositiveIntegerField(help_text='أدخل سنة الصنع السيارة.', null=True, verbose_name='سنة الصنع'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='model',
            field=models.CharField(help_text='أدخل موديل السيارة بشكل دقيق.', max_length=50, verbose_name='موديل السيارة'),
        ),
    ]
