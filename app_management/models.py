

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
class Province(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    employee_no = models.CharField(max_length=255)
    store_id = models.IntegerField()
    mcdelivery = models.BooleanField()
    drive_other = models.BooleanField()
    drive_other_desc = models.CharField(max_length=255, blank=True, null=True)
    del_trans_id = models.IntegerField()
    delivery_date = models.DateTimeField()
    delivery_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'delivery'



class Drivecampaign(models.Model):
    drivecampaign_id = models.IntegerField(primary_key=True)
    campaign_name = models.CharField(max_length=255)
    campaign_price = models.CharField(max_length=255, blank=True, null=True)
    campaign_status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'drivecampaign'


class Drivethru(models.Model):
    employee_no = models.CharField(max_length=255)
    store_id = models.IntegerField()
    is_drivethru = models.BooleanField()
    drive_menu = models.CharField(max_length=255, blank=True, null=True)
    drive_menu_board = models.BooleanField()
    drive_menu_board_desc = models.CharField(max_length=255, blank=True, null=True)
    drive_menu_board_campaign_layout = models.BooleanField()
    drive_menu_board_campaign_layout_desc = models.CharField(max_length=255, blank=True, null=True)
    drive_menu_board_layout_campaign_list = models.TextField(blank=True, null=True)  # This field type is a guess.
    drive_cod_layout = models.BooleanField()
    drive_cod_layout_desc = models.CharField(max_length=255, blank=True, null=True)
    drive_advert = models.BooleanField()
    drive_advert_desc = models.CharField(max_length=255, blank=True, null=True)
    drive_trans_id = models.IntegerField()
    drivethru_date = models.DateTimeField()
    drivethru_id = models.AutoField(primary_key=True)

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

class Happymealcampaign(models.Model):
    happymealcampaign_id = models.IntegerField(primary_key=True)
    campaign_name = models.CharField(max_length=255)
    campaign_price = models.CharField(max_length=255, blank=True, null=True)
    campaign_status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'happymealcampaign'

class Inside(models.Model):
    employee_no = models.CharField(max_length=255)
    store_id = models.IntegerField()
    inside_trans_id = models.IntegerField()
    inside_entry_campaigns = models.BooleanField()
    inside_entry_campaigns_list = models.TextField(blank=True, null=True)  # This field type is a guess.
    inside_music = models.BooleanField()
    inside_television = models.BooleanField()
    inside_television_number = models.IntegerField(blank=True, null=True)
    inside_television_number_work = models.IntegerField(blank=True, null=True)
    inside_sok_layout = models.CharField(max_length=255, blank=True, null=True)
    inside_sok_layout_desc = models.CharField(max_length=255, blank=True, null=True)
    inside_sok_campaigns_list = models.TextField(blank=True, null=True)  # This field type is a guess.
    inside_mystore_campaigns = models.BooleanField()
    inside_mystore_image_url = models.CharField(max_length=255, blank=True, null=True)
    inside_happymeal_layout = models.BooleanField()
    inside_happymeal_layout_desc = models.CharField(max_length=255)
    inside_happymeal_campaigns_list = models.TextField(blank=True, null=True)  # This field type is a guess.
    inside_description = models.CharField(max_length=255)
    inside_date = models.DateTimeField(blank=True, null=True)
    inside_id = models.AutoField(primary_key=True)
    inside_avail_sok = models.CharField(max_length=255)
    inside_avail_sok_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inside'

class Insidecampaign(models.Model):
    inside_id = models.IntegerField(primary_key=True)
    campaign_name = models.CharField(max_length=255)
    campaign_price = models.CharField(max_length=255, blank=True, null=True)
    campaign_status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'insidecampaign'

class Mccafe(models.Model):
    mccafe_id = models.AutoField(primary_key=True)
    employee_no = models.CharField(max_length=255)
    store_id = models.IntegerField()
    mccafe_trans_id = models.IntegerField()
    mccafe_menu = models.CharField(max_length=255)
    mccafe_model = models.CharField(max_length=255)
    mccafe_menu_display = models.BooleanField()
    mccafe_menu_display_desc = models.CharField(max_length=255, blank=True, null=True)
    mccafe_menu_board_campaign_layout = models.BooleanField()
    mccafe_menu_board_campaign_layout_desc = models.CharField(max_length=255, blank=True, null=True)
    mccafe_menu_board_layout_campaign_list = models.TextField(blank=True, null=True)  # This field type is a guess.
    mccafe_date = models.DateTimeField(db_column='mcCafe_date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mcCafe'

class Mccafecampaign(models.Model):
    mccafecampaign_id = models.IntegerField(primary_key=True)
    campaign_name = models.CharField(max_length=255)
    campaign_price = models.CharField(max_length=255, blank=True, null=True)
    campaign_status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mccafecampaign'
class Menu(models.Model):
    employee_no = models.CharField(max_length=255)
    store_id = models.IntegerField()
    menu_display = models.CharField(max_length=255)
    menu_pop_layout = models.BooleanField()
    menu_pop_layout_desc = models.CharField(max_length=255, blank=True, null=True)
    menu_pricepoint = models.TextField()  # This field type is a guess.
    menu_board_display = models.BooleanField()
    menu_board_display_desc = models.CharField(max_length=255, blank=True, null=True)
    menu_board_campaign_layout = models.BooleanField()
    menu_board_campaign_layout_desc = models.CharField(max_length=255, blank=True, null=True)
    menu_board_campaig_list = models.TextField(blank=True, null=True)  # This field type is a guess.
    menu_trans_id = models.IntegerField()
    menu_date = models.DateTimeField()
    menu_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'menu'

class Menucampaign(models.Model):
    menucampaign_id = models.IntegerField(primary_key=True)
    campaign_name = models.CharField(max_length=255)
    campaign_price = models.CharField(max_length=255, blank=True, null=True)
    campaign_status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'menucampaign'


class Outside(models.Model):
    employee_no = models.CharField(max_length=255)
    store_id = models.IntegerField()
    outside_trans_id = models.IntegerField()
    outside_promotions = models.BooleanField()
    outside_promotions_desc = models.CharField(max_length=255, blank=True, null=True)
    outside_image_url = models.CharField(max_length=255, blank=True, null=True)
    outside_date = models.DateTimeField(blank=True, null=True)
    outside_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'outside'



class Sokcampaign(models.Model):
    sokcampaign_id = models.IntegerField(primary_key=True)
    campaign_name = models.CharField(max_length=255)
    campaign_price = models.CharField(max_length=255, blank=True, null=True)
    campaign_status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sokcampaign'


class Shops(models.Model):
    store_id = models.AutoField(primary_key=True)
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
