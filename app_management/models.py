from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.province}"

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


class EntranceEvaluation(models.Model):
    province = models.TextField(blank=True, null=True)
    store= models.TextField(blank=True, null=True)
    branding_condition = models.CharField(max_length=3, blank=True)
    disclaimer_signage_condition = models.CharField(max_length=3, )
    noticed_campaigns = models.CharField(max_length=3, blank=True)
    campaign_details = models.TextField(blank=True, null=True)
    additional_comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Entrance Evaluation #{self.id}'



class Store_level(models.Model):
    site_name = models.CharField(max_length=255,blank=True)
    mc_dim_no = models.CharField(max_length=255, unique=True,blank=True)
    restaurant = models.CharField(max_length=255)
    physical_address = models.CharField(max_length=255)
    tel_no = models.CharField(max_length=255,blank=True)
    owner = models.CharField(max_length=255)
    ops_manager = models.CharField(max_length=255)
    franchise_manager = models.CharField(max_length=255)
    franchise_mcopco = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    coordinates = models.CharField(max_length=255)
    region = models.ForeignKey(Province, on_delete=models.CASCADE,blank=True,null=True,default=None)

    def __str__(self):
        return f"{self.site_name} - {self.region}"


class Employee(models.Model):
    employee_no = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    id_number = models.CharField(max_length=14)
    email_address = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    employment_status = models.CharField(max_length=50)
    start_day = models.DateField(default=models.DateField(auto_now_add=True))
    end_date = models.DateField(null=True, blank=True)

class Outside(models.Model):
    employee_no = models.CharField(max_length=255)
    mc_dim_no = models.CharField(max_length=255,blank=True)
    outside_trans_id = models.DecimalField(max_digits=255, decimal_places=0)
    branding_condition= models.BooleanField()
    signage_condition = models.BooleanField()
    campaign = models.BooleanField()
    campaigns = models.CharField(max_length=255,blank=True,default='Null')
    outside_date = models.DateField(default=models.DateField(auto_now_add=True))
    description_outside = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    store = models.ForeignKey(Store_level, on_delete=models.CASCADE)

# Define other models (Inside, Menu, McCafe, Delivery, Drivethru) similarly...
class Inside(models.Model):
    employee_no = models.CharField(max_length=255)
    mc_dim_no = models.CharField(max_length=255,blank=True)
    inside_trans_id = models.DecimalField(max_digits=255, decimal_places=0)
    point_of_sale = models.BooleanField()
    pop_description = models.CharField(max_length=255,blank=True)
    self_order_kiosk = models.BooleanField()
    promo_sok_campaigns = models.CharField(max_length=1255,blank=True,default='Null')
    promotion_image_url = models.CharField(max_length=255,blank=True)
    happy_m_campaign = models.CharField(max_length=255)
    description_inside = models.CharField(max_length=255)
    inside_date = models.DateField(default=models.DateField(auto_now_add=True))
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    store = models.ForeignKey(Store_level, on_delete=models.CASCADE)

class Menu(models.Model):
    employee_no = models.CharField(max_length=255)
    mc_dim_no = models.CharField(max_length=255,blank=True)
    menu_trans_id = models.DecimalField(max_digits=255, decimal_places=0)
    menu_visibility = models.BooleanField()
    price_visibility = models.CharField(max_length=255)
    menu_promotion = models.CharField(max_length=255,blank=True)
    description_menu = models.CharField(max_length=255)
    menu_date = models.DateField(default=models.DateField(auto_now_add=True))
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    store = models.ForeignKey(Store_level, on_delete=models.CASCADE)

class McCafe(models.Model):
    employee_no = models.CharField(max_length=255)
    mc_dim_no = models.CharField(max_length=255,blank=True)
    mc_trans_id = models.DecimalField(max_digits=255, decimal_places=0)
    menu_visibility = models.BooleanField()
    menu_promo = models.CharField(max_length=255,blank=True)
    description_mccafe = models.CharField(max_length=255)
    mccafe_date = models.DateField(default=models.DateField(auto_now_add=True))
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    store = models.ForeignKey(Store_level, on_delete=models.CASCADE)

class Delivery(models.Model):
    employee_no = models.CharField(max_length=255)
    mc_dim_no = models.CharField(max_length=255,blank=True)
    del_trans_id = models.DecimalField(max_digits=255, decimal_places=0)
    mc_delivery = models.BooleanField()
    third_party_del = models.BooleanField()
    description_delivery = models.CharField(max_length=255)
    delivery_date = models.DateField(default=models.DateField(auto_now_add=True))
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    store = models.ForeignKey(Store_level, on_delete=models.CASCADE)

class Drivethru(models.Model):
    employee_no = models.CharField(max_length=255)
    mc_dim_no = models.CharField(max_length=255,blank=True)
    drive_trans_id = models.DecimalField(max_digits=255, decimal_places=0)
    drivethru_campaign = models.CharField(max_length=255,blank=True)
    customer_order_display = models.CharField(max_length=255,blank=True)
    activation_on_promo = models.BooleanField()
    activation_description = models.CharField(max_length=255)
    drivethru_date = models.DateField(default=models.DateField(auto_now_add=True))
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    store = models.ForeignKey(Store_level, on_delete=models.CASCADE)
