# Generated by Django 3.2.20 on 2023-12-28 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_management', '0025_alter_outside_outside_trans_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inside',
            name='mc_dim_no',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='outside',
            name='outside_trans_id',
            field=models.DecimalField(decimal_places=0, max_digits=255),
        ),
    ]
