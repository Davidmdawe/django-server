
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
class Province(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name



class Store_Map(models.Model):
    name = models.CharField(max_length=255)
    lat = models.FloatField()
    lon = models.FloatField()
    province = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class StorePerformance(models.Model):
    store = models.OneToOneField(Store_Map, on_delete=models.CASCADE)
    target = models.IntegerField()
    achieved = models.IntegerField()

    def __str__(self):
        return f"{self.store.name} - Target: {self.target}, Achieved: {self.achieved}"



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Copyemployee(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)
    employee_no = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    id_number = models.CharField(max_length=255, blank=True, null=True)
    email_address = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    employment_status = models.CharField(max_length=255, blank=True, null=True)
    start_day = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    cellphone_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'copyemployee'


class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    employee_no = models.ForeignKey('Employee', models.DO_NOTHING, db_column='employee_no', blank=True, null=True)
    del_trans_id = models.IntegerField()
    third_party_del = models.BooleanField(blank=True, null=True)
    description_delivery = models.CharField(max_length=255, blank=True, null=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    store_id = models.IntegerField()
    mcdelivery = models.BooleanField(db_column='McDelivery', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'delivery'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Drivethru(models.Model):
    drivethru_id = models.AutoField(primary_key=True)
    employee_no = models.ForeignKey('Employee', models.DO_NOTHING, db_column='employee_no')
    drive_trans_id = models.IntegerField()
    drivethru_campaign = models.TextField()  # This field type is a guess.
    activation_on_promo = models.BooleanField()
    activation_description = models.CharField(max_length=255)
    drivethru_date = models.DateTimeField(blank=True, null=True)
    store_id = models.IntegerField()
    customer_order_display = models.CharField(db_column='Customer_order_display', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'drivethru'


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_no = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255)
    email_address = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    employment_status = models.CharField(max_length=255)
    start_day = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    cellphone_number = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'employee'


class Inside(models.Model):
    inside_id = models.AutoField(primary_key=True)
    employee_no = models.ForeignKey(Employee, models.DO_NOTHING, db_column='employee_no')
    inside_trans_id = models.IntegerField()
    promo_sok_campaigns_list = models.TextField()  # This field type is a guess.
    description_inside = models.CharField(max_length=255)
    inside_date = models.DateTimeField(blank=True, null=True)
    store_id = models.IntegerField()
    pop_description = models.CharField(max_length=255)
    point_of_purchase = models.BooleanField()
    self_order_kiosk = models.CharField(max_length=255)
    happy_m_campaign = models.TextField()  # This field type is a guess.
    mystorecamp_image_url = models.CharField(max_length=255, blank=True, null=True)
    insidemystorecamp = models.BooleanField(db_column='insideMyStoreCamp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inside'


class Mccafe(models.Model):
    mccafe_id = models.AutoField(db_column='mcCafe_id', primary_key=True)  # Field name made lowercase.
    employee_no = models.CharField(max_length=255)
    store_id = models.IntegerField()
    mc_trans_id = models.IntegerField()
    menu_visibility = models.BooleanField()
    description_mccafe = models.CharField(max_length=255)
    mccafe_date = models.DateTimeField(db_column='mcCafe_date', blank=True, null=True)  # Field name made lowercase.
    digital_menu_mc = models.CharField(max_length=255, blank=True, null=True)
    menu_promo = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mcCafe'


class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    employee_no = models.ForeignKey(Employee, models.DO_NOTHING, db_column='employee_no')
    menu_trans_id = models.IntegerField()
    menu_visibility = models.BooleanField()
    menu_promotion = models.TextField()  # This field type is a guess.
    description_menu = models.CharField(max_length=255)
    menu_date = models.DateTimeField(blank=True, null=True)
    store_id = models.IntegerField()
    price_visibility = models.TextField()  # This field type is a guess.
    digital_menu = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class Outside(models.Model):
    outside_id = models.AutoField(primary_key=True)
    employee_no = models.ForeignKey(Employee, models.DO_NOTHING, db_column='employee_no')
    outside_trans_id = models.IntegerField()
    disclaimer = models.BooleanField()
    campaigns = models.BooleanField()
    campaigns_list = models.TextField()  # This field type is a guess.
    outside_date = models.DateTimeField(blank=True, null=True)
    description_outside = models.CharField(max_length=255)
    store_id = models.IntegerField()
    outsidemystorecamp = models.BooleanField(db_column='outsideMyStoreCamp', blank=True, null=True)  # Field name made lowercase.
    mystorecamp_img_url = models.CharField(max_length=255, blank=True, null=True)
    signage_condition = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outside'


class Shops(models.Model):
    store_id = models.IntegerField(primary_key=True)
    site_name = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    districr = models.CharField(max_length=255, blank=True, null=True)
    municipality = models.CharField(max_length=255, blank=True, null=True)
    store_type = models.CharField(max_length=255, blank=True, null=True)
    portfolio_type = models.CharField(max_length=255, blank=True, null=True)
    open_date = models.CharField(max_length=255, blank=True, null=True)
    close_date = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shops'


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    site_name = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    mcdim_no = models.DecimalField(unique=True, max_digits=255, decimal_places=0, blank=True, null=True)
    restaurant = models.CharField(max_length=255, blank=True, null=True)
    physical_address = models.CharField(max_length=255, blank=True, null=True)
    tel_no = models.CharField(max_length=255, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    ops_manager = models.CharField(max_length=255, blank=True, null=True)
    franchise_manager = models.CharField(max_length=255, blank=True, null=True)
    franchise_mcopco = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    cordinates = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store'
