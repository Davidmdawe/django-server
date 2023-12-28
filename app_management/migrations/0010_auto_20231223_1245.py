# Generated by Django 3.2.20 on 2023-12-23 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_management', '0009_auto_20231217_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_no', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('id_number', models.CharField(max_length=14)),
                ('email_address', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('employment_status', models.CharField(max_length=50)),
                ('start_day', models.DateField(default=models.DateField(auto_now_add=True))),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='storeperformance',
            name='store',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_management.store'),
        ),
        migrations.CreateModel(
            name='Store_level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(blank=True, max_length=255)),
                ('mc_dim_no', models.DecimalField(decimal_places=0, max_digits=255, unique=True)),
                ('restaurant', models.CharField(max_length=255)),
                ('physical_address', models.CharField(max_length=255)),
                ('tel_no', models.CharField(max_length=255)),
                ('owner', models.CharField(max_length=255)),
                ('ops_manager', models.CharField(max_length=255)),
                ('franchise_manager', models.CharField(max_length=255)),
                ('franchise_mcopco', models.CharField(max_length=255)),
                ('latitude', models.CharField(max_length=255)),
                ('longitude', models.CharField(max_length=255)),
                ('coordinates', models.CharField(max_length=255)),
                ('region', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_management.province')),
            ],
        ),
        migrations.CreateModel(
            name='Outside',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_no', models.CharField(max_length=255)),
                ('mc_dim_no', models.DecimalField(decimal_places=0, max_digits=255)),
                ('outside_trans_id', models.DecimalField(decimal_places=0, max_digits=255)),
                ('signage_condition', models.BooleanField()),
                ('campaign', models.BooleanField(blank=True, default=0)),
                ('campaigns', models.CharField(blank=True, default='Null', max_length=255)),
                ('outside_date', models.DateField(default=models.DateField(auto_now_add=True))),
                ('description_outside', models.CharField(max_length=255)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_management.employee')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_management.store')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_no', models.CharField(max_length=255)),
                ('mc_dim_no', models.DecimalField(decimal_places=0, max_digits=255)),
                ('menu_trans_id', models.DecimalField(decimal_places=0, max_digits=255)),
                ('menu_visibility', models.BooleanField()),
                ('price_visibility', models.CharField(max_length=255)),
                ('menu_promotion', models.CharField(blank=True, max_length=255)),
                ('description_menu', models.CharField(max_length=255)),
                ('menu_date', models.DateField(default=models.DateField(auto_now_add=True))),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_management.employee')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_management.store')),
            ],
        ),
        migrations.CreateModel(
            name='McCafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_no', models.CharField(max_length=255)),
                ('mc_dim_no', models.DecimalField(decimal_places=0, max_digits=255)),
                ('mc_trans_id', models.DecimalField(decimal_places=0, max_digits=255)),
                ('menu_visibility', models.BooleanField()),
                ('menu_promo', models.CharField(blank=True, max_length=255)),
                ('description_mccafe', models.CharField(max_length=255)),
                ('mccafe_date', models.DateField(default=models.DateField(auto_now_add=True))),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_management.employee')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_management.store')),
            ],
        ),
        migrations.CreateModel(
            name='Inside',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_no', models.CharField(max_length=255)),
                ('mc_dim_no', models.DecimalField(decimal_places=0, max_digits=255)),
                ('inside_trans_id', models.DecimalField(decimal_places=0, max_digits=255)),
                ('point_of_sale', models.BooleanField()),
                ('pop_description', models.CharField(max_length=255)),
                ('self_order_kiosk', models.BooleanField()),
                ('promo_sok_campaigns', models.CharField(blank=True, default='Null', max_length=255)),
                ('promotion_image_url', models.CharField(max_length=255)),
                ('happy_m_campaign', models.CharField(max_length=255)),
                ('description_inside', models.CharField(max_length=255)),
                ('inside_date', models.DateField(default=models.DateField(auto_now_add=True))),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_management.employee')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_management.store')),
            ],
        ),
        migrations.CreateModel(
            name='Drivethru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_no', models.CharField(max_length=255)),
                ('mc_dim_no', models.DecimalField(decimal_places=0, max_digits=255)),
                ('drive_trans_id', models.DecimalField(decimal_places=0, max_digits=255)),
                ('drivethru_campaign', models.CharField(blank=True, max_length=255)),
                ('customer_order_display', models.CharField(blank=True, max_length=255)),
                ('activation_on_promo', models.BooleanField()),
                ('activation_description', models.CharField(max_length=255)),
                ('drivethru_date', models.DateField(default=models.DateField(auto_now_add=True))),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_management.employee')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_management.store')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_no', models.CharField(max_length=255)),
                ('mc_dim_no', models.DecimalField(decimal_places=0, max_digits=255)),
                ('del_trans_id', models.DecimalField(decimal_places=0, max_digits=255)),
                ('mc_delivery', models.BooleanField()),
                ('third_party_del', models.BooleanField()),
                ('description_delivery', models.CharField(max_length=255)),
                ('delivery_date', models.DateField(default=models.DateField(auto_now_add=True))),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_management.employee')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_management.store')),
            ],
        ),
    ]
