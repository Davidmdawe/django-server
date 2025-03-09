from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import Province,Shops as Store_level,Inside,Outside,Menu,Mccafe as McCafe,Drivethru as Drivethru,Delivery as Delivery # Import the Province model
from django.http import JsonResponse
import random
import calendar
from django.views import View
from datetime import datetime, timedelta
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.timezone import make_aware
from .filters import ShopsFilter
import pytz




def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            # Redirect to the home page
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')

    return render(request, 'login.html')

def get_month_date_range(month):
    if month and "_" in month:
        month_name, year = month.split("_")
        month_number = list(calendar.month_name).index(month_name.capitalize())

        # Get the first and last day of the month
        _, last_day = calendar.monthrange(int(year), month_number)

        # Create a timezone object (adjust to your project's timezone)
        timezone = pytz.timezone('UTC')

        # Generate the start date for the month (beginning of the month)
        start_date = timezone.localize(datetime(int(year), month_number, 1, 0, 0, 0))

        # Generate the end date as the last day of the month
        end_date = timezone.localize(datetime(int(year), month_number, last_day, 23, 59, 59))

        return start_date, end_date
    return None, None
@login_required()
def home_view(request):
    provinces = Province.objects.all()  # Retrieve all provinces from the database
    user = request.user
    username=user.username
    region_name = Store_level.objects.values('region').distinct()
    franchise_mcopco = Store_level.objects.values('portfolio_type').distinct()
    ids=Menu.objects.values('store_id')
    #restaurant= Store_level.objects.values('site_name').distinct()
    #########
    start_month = 'January_2025'
    end_month = 'March_2025'

    # Get the start date for June 2024
    june_start, _ = get_month_date_range(start_month)
    # Get the end date for July 2024
    _, july_end = get_month_date_range(end_month)

    # Set the used start and end dates
    start_date_used = june_start
    end_date_used = july_end

    print("Start Date:", start_date_used)
    print("End Date:", end_date_used)
    
    #######
    restaurant= Store_level.objects.filter(store_id__in=ids).values('site_name','store_id',)
    # Get all store IDs from Menu model
    
    all_store_ids = Menu.objects.filter(
        menu_date__gte=start_date_used,menu_date__lte=end_date_used
    ).values_list('store_id', flat=True).distinct()
    # Filter store details from Shops model where the region is Gauteng
    gauteng_stores = Store_level.objects.filter(store_id__in=all_store_ids, region='GAUTENG')

    # Count the number of stores in Gauteng
    num_gauteng_stores = gauteng_stores.count()

    # Filter store details from Shops model where the region is Gauteng
    FREE_STATE_stores = Store_level.objects.filter(store_id__in=all_store_ids, region='FREE STATE')

    # Count the number of stores in Gauteng
    num_FREE_STATE_stores = FREE_STATE_stores.count()

    EASTERN_CAPE_stores = Store_level.objects.filter(store_id__in=all_store_ids, region='EASTERN CAPE')

    # Count the number of stores in Gauteng
    num_EASTERN_CAPE_stores = EASTERN_CAPE_stores.count()

    KWAZULU_NATAL_stores = Store_level.objects.filter(store_id__in=all_store_ids, region='KWAZULU-NATAL')

    # Count the number of stores in Gauteng
    num_KWAZULU_NATAL_stores = KWAZULU_NATAL_stores.count()
    LIMPOPO_stores = Store_level.objects.filter(store_id__in=all_store_ids, region='LIMPOPO')

    # Count the number of stores in Gauteng
    num_LIMPOPO_stores = LIMPOPO_stores.count()
    MPUMALANGA_stores = Store_level.objects.filter(store_id__in=all_store_ids, region='MPUMALANGA')

    # Count the number of stores in Gauteng
    num_MPUMALANGA_stores = MPUMALANGA_stores.count()
    NORTH_WEST_stores = Store_level.objects.filter(store_id__in=all_store_ids, region='NORTH WEST')

    # Count the number of stores in Gauteng
    num_NORTH_WEST_stores = NORTH_WEST_stores.count()

    NORTHERN_CAPE_stores = Store_level.objects.filter(store_id__in=all_store_ids, region='NORTHERN CAPE')

    # Count the number of stores in Gauteng
    num_NORTHERN_CAPE_stores =NORTHERN_CAPE_stores.count()
    WESTERN_CAPE_stores = Store_level.objects.filter(store_id__in=all_store_ids, region='WESTERN CAPE')

    # Count the number of stores in Gauteng
    num_WESTERN_CAPE_stores =WESTERN_CAPE_stores.count()

    province_ids = Menu.objects.filter(
        menu_date__gte=start_date_used,menu_date__lte=end_date_used
    ).values('store_id')
    restaurant_province = Store_level.objects.filter(store_id__in=province_ids).all()
    shop_filter = ShopsFilter(request.GET, queryset=restaurant_province)

    total_stores=num_WESTERN_CAPE_stores+num_NORTHERN_CAPE_stores+num_NORTH_WEST_stores +num_LIMPOPO_stores+num_KWAZULU_NATAL_stores+num_EASTERN_CAPE_stores+num_FREE_STATE_stores+num_gauteng_stores
    print(f'Number of stores in Gauteng: {total_stores}')
    
    
    context = {'filter': shop_filter,'provinces': provinces,'total_stores':total_stores,'num_NORTHERN_CAPE_stores':num_NORTHERN_CAPE_stores,'num_WESTERN_CAPE_stores':num_WESTERN_CAPE_stores,'num_NORTH_WEST_stores':num_NORTH_WEST_stores,'num_MPUMALANGA_stores':num_MPUMALANGA_stores,'num_LIMPOPO_stores':num_LIMPOPO_stores,'num_KWAZULU_NATAL_stores':num_KWAZULU_NATAL_stores,'num_EASTERN_CAPE_stores':num_EASTERN_CAPE_stores,'num_FREE_STATE_stores':num_FREE_STATE_stores,'num_gauteng_stores':num_gauteng_stores,'username':username,'franchise_mcopco':franchise_mcopco,'restaurant':restaurant,'region_name':region_name}
    return render(request, 'home.html', context)
    
@login_required
def visuals_view(request):
    provinces = Province.objects.all()
    user = request.user
    username = user.username

    province_ids = Menu.objects.values('store_id')
    restaurant_province = Store_level.objects.filter(store_id__in=province_ids).all()
    shop_filter = ShopsFilter(request.GET, queryset=restaurant_province)

    context = {'filter': shop_filter,'provinces':provinces}

    return render(request, 'visuals.html', context)

def get_stores(request):
    month = request.GET.get('month')
    province = request.GET.get('province')
    if month and "_" in month:
        month_name, year = month.split("_")
        month_number = list(calendar.month_name).index(month_name.capitalize())

        # Get the first and last day of the month
        _, last_day = calendar.monthrange(int(year), month_number)

        # Create a timezone object (adjust to your project's timezone)
        timezone = pytz.timezone('UTC')

        # Generate the start date for the month (beginning of the month)
        start_date = timezone.localize(datetime(int(year), month_number, 1, 0, 0, 0))

        # Generate the end date as the day before today
        today = datetime.now(timezone)
        if today.year == int(year) and today.month == month_number:
            end_date = today - timedelta(days=1)
        else:
            # If today is not within the month in question, use the last day of the month
            end_date = timezone.localize(datetime(int(year), month_number, last_day, 23, 59, 59))
        print('Start')
        print(start_date)
        print('End')
        print(end_date)
        
        store_ids = Menu.objects.filter(menu_date__gte=start_date, menu_date__lte=end_date).values('store_id')
        restaurant = Store_level.objects.filter(store_id__in=store_ids, region=province).values("site_name", "store_id").distinct()
        store_list = list(restaurant)
    else:
        store_list = []

    return JsonResponse(store_list, safe=False)

def get_provinces(request):
    month = request.GET.get('month')
    if month and "_" in month:
        month_name, year = month.split("_")
        month_number = list(calendar.month_name).index(month_name.capitalize())

        # Get the first and last day of the month
        _, last_day = calendar.monthrange(int(year), month_number)

        # Create a timezone object (adjust to your project's timezone)
        timezone = pytz.timezone('UTC')

        # Generate the start date for the month (beginning of the month)
        start_date = timezone.localize(datetime(int(year), month_number, 1, 0, 0, 0))

        # Generate the end date as the day before today
        today = datetime.now(timezone)
        if today.year == int(year) and today.month == month_number:
            end_date = today - timedelta(days=1)
        else:
            # If today is not within the month in question, use the last day of the month
            end_date = timezone.localize(datetime(int(year), month_number, last_day, 23, 59, 59))

        

        store_ids = Menu.objects.filter(menu_date__gte=start_date, menu_date__lte=end_date).values('store_id')
        restaurant_province = Store_level.objects.filter(store_id__in=store_ids).values("region").distinct()
        provinces_list = list(restaurant_province)
    else:
        provinces_list = []

    return JsonResponse(provinces_list, safe=False)



@login_required()
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to your login page

@login_required()   
def get_store_data(request):
    selected_province = request.GET.get('province', 'all')
    month = request.GET.get('month', None)
    print()
    if month and "_" in month:
        month_name, year = month.split("_")
        month_number = list(calendar.month_name).index(month_name.capitalize())

        # Get the first and last day of the month
        _, last_day = calendar.monthrange(int(year), month_number)

        # Create a timezone object (adjust to your project's timezone)
        timezone = pytz.timezone('UTC')

        # Generate a list of datetime objects for the entire month (with timezone awareness)
        start_date = timezone.localize(datetime(int(year), month_number, 1, 0, 0, 0))
        end_date = timezone.localize(datetime(int(year), month_number, last_day, 23, 59, 59))
    stores_ids=Menu.objects.values('store_id')
    try:
        data = []  # Initialize the data list
        if selected_province == 'all':
            stores = Store_level.objects.values('site_name', 'latitude', 'longitude', 'region')

        else:
            stores = Store_level.objects.filter(region=selected_province,store_id__in=stores_ids).values('site_name', 'latitude', 'longitude', 'region')

        # Convert QuerySet to a list of dictionaries
        stores_list = list(stores)
        for store in stores_list:
            data.append({
                'site_name': store['site_name'],
                'latitude': str(store['latitude']),
                'longitude': str(store['longitude']),
                'region': store['region'],
                'selected_province': selected_province
            })
        
        return JsonResponse(data, safe=False)
    except Exception as e:
        # Log the error and handle it appropriately
        print(f"Error retrieving data: {e}")
        return JsonResponse({'error': 'An error occurred while retrieving data.'}, status=500)
        
 

class MapDataView(View):
    def get(self, request, *args, **kwargs):
        selected_province_store = request.GET.get('province_store', 'all')
        selected_stire_franchise = request.GET.get('owner_franchise', 'all')
        selected_store = request.GET.get('store', '')
        from_date = request.GET.get('from_date', None)
        to_date = request.GET.get('to_date', None)
        if selected_store  == 'all':
           store_data = Store_level.objects.values('site_name', 'latitude', 'longitude','physical_address','tel_no','region__name')
        else:
           store_data = Store_level.objects.filter(site_name=selected_store).values('site_name', 'latitude', 'longitude','physical_address','tel_no','region__name')
        return JsonResponse(list(store_data), safe=False)
import calendar
import pytz
@login_required()
def get_store_data_store_level(request):
    selected_province_store = request.GET.get('province_store', 'all')
    selected_store = request.GET.get('store', 'all')
    #selected_store=1
    site_name=Store_level.objects.filter(store_id=selected_store).values('site_name')
    selected_store_name= site_name[0]['site_name'] if site_name else None
    month = request.GET.get('month', None)
    if month and "_" in month:
        month_name, year = month.split("_")
        month_number = list(calendar.month_name).index(month_name.capitalize())

        # Get the first and last day of the month
        _, last_day = calendar.monthrange(int(year), month_number)

        # Create a timezone object (adjust to your project's timezone)
        timezone = pytz.timezone('UTC')

        # Generate a list of datetime objects for the entire month (with timezone awareness)
        start_date = timezone.localize(datetime(int(year), month_number, 1, 0, 0, 0))
        end_date = timezone.localize(datetime(int(year), month_number, last_day, 23, 59, 59))
    dates_in_month=''
    data = []
    total_score_outside = 0 
    total_score_inside=0 # Initialize total_score_outside outside the loop
    total_score_Main=0
    target_outside = 4
    total_score_Mccafe=0
    target_mccafe = 2
    target_delivery = 2
    target_drivethru = 3
    target_inside=4
    target_menu=3
    out_branding_condition = 0  # Initialize out_branding_condition
    out_signage_condition = 0  # Initialize out_signage_condition
    out_point_of_sale=0
    out_self_order_kiosk=0
    menu_visibility=0
    out_campaign = 0  # Initialize out_campaign
    out_campaigns=''
    out_description_outside=0
    out_happy_m_campaign=''
    out_description_inside=0
    out_promo_sok_campaigns=0
    price_visibility=0
    menu_promotion=''
    description_menu=0
    mccafemenu_visibility_score=0
    mccafemenu_visibility=0
    menu_promo=0
    activation_on_promo=0
    description_mccafe=0
    total_score_drivethru=0
    drivethru_campaign=''
    customer_order_display=0
    activation_description=0
    total_score_delivery=0
    insidemystorecamp=0
    mc_delivery=0
    third_party_del=0
    description_delivery=0
    description_menu_store_site_name=0
    description_menu_date=0
    description_menu_store_site_name=0
    out_pop_description_inside=0
    mccafe_store_site_name=0
    mccafe_date=0
    drivethru_date=0
    drive_store_site_name=0
    store_site_name=0
    delivery_date=0
    out_campaign_outside_store_site_name=0
    out_campaign_outside_date=0
    out_store_site_name=0
    out_description_inside_date=0
    outsidemystorecamp=0
    mystorecamp_img_url=0
    digital_menu_mc=0
    digital_menu=0
    outside_promotions_score=0
    outside_promotions=''
    outside_promotions_desc=''
    inside_date=''
    outside_image_url=''
    inside_mystore_image_url=''
    inside_television=''
    inside_music=''
    inside_entry_campaigns=''
    inside_entry_campaigns_list=''
    inside_entry_campaigns_score=0
    inside_music_score =0
    inside_television_score =0
    inside_avail_sok_score =0
    inside_happymeal_layout_score =0
    inside_sok_layout_score =0
    inside_television_number=''
    inside_television_number_work=''
    inside_avail_sok=''
    inside_sok_layout=''
    inside_sok_layout_desc=''
    inside_sok_campaigns_list=''
    inside_mystore_campaigns=''
    inside_happymeal_layout=''
    inside_happymeal_layout_desc=''
    inside_happymeal_campaigns_list=''
    menu_date=''
    menu_pricepoint=''
    menu_pop_layout=''
    menu_board_display=''
    menu_pop_layout_desc=''
    menu_board_display_desc=''
    menu_board_campaign_layout=''
    menu_board_campaign_layout_desc=''
    menu_board_campaig_list=''
    mccafe_model=''
    mccafe_menu=''
    mccafe_menu_display=''
    mccafe_menu_display_desc=''
    mccafe_menu_board_campaign_layout=''
    mccafe_menu_board_campaign_layout_desc=''
    mccafe_menu_board_layout_campaign_list=''
    is_drivethru=''
    drive_menu=''
    drive_menu_board=''
    drive_menu_board_desc=''
    drive_menu_board_campaign_layout=''
    drive_menu_board_campaign_layout_desc=''
    drive_menu_board_layout_campaign_list=''
    drive_cod_layout=''
    drive_cod_layout_desc=''
    drive_advert=''
    drive_advert_desc=''
    drive_cod_layout_score=0
    mcdelivery=''
    drive_other=''
    Outqueryset = Outside.objects.filter(
        store_id=selected_store,
        outside_date__gte=start_date,
        outside_date__lte=end_date
    ).values(
        'employee_no',
        'store_id',
        'outside_trans_id',
        'outside_promotions',
        'outside_promotions_desc',
        'outside_image_url',
        'outside_date',
        'outside_id'
    ).last()
    if Outqueryset:
        item = Outqueryset 
        outside_promotions_score = 1 if item['outside_promotions'] else 0
        outside_promotions = item['outside_promotions']
        outside_promotions_desc = item['outside_promotions_desc']
        outside_image_url = item['outside_image_url']
        out_campaign_outside_date = item['outside_date']
        store_id = item['store_id']
        site_name_store = Store_level.objects.filter(store_id=store_id).values('site_name')
        selected_store_name_store = site_name_store[0]['site_name'] if site_name_store else None
        out_campaign_outside_store_site_name = selected_store_name_store
        total_score_outside +=outside_promotions_score
    else:
        print("No records found within the specified date range.")

    Inqueryset = Inside.objects.filter(store_id=selected_store,inside_date__gte=start_date,inside_date__lte=end_date).values(
    'employee_no',
    'store_id',
    'inside_trans_id',
    'inside_entry_campaigns',
    'inside_entry_campaigns_list',
    'inside_music',
    'inside_television',
    'inside_television_number',
    'inside_television_number_work',
    'inside_sok_layout',
    'inside_sok_layout_desc',
    'inside_sok_campaigns_list',
    'inside_mystore_campaigns',
    'inside_mystore_image_url',
    'inside_happymeal_layout',
    'inside_happymeal_layout_desc',
    'inside_happymeal_campaigns_list',
    'inside_description',
    'inside_date',
    'inside_id',
    'inside_avail_sok',
    'inside_avail_sok_desc').last()
    if Inqueryset:
        item =Inqueryset
        inside_music_score = 1 if item['inside_music'] else 0
        #inside_television_score = 1 if item['inside_television'] else 0
        inside_avail_sok_score = 1 if item['inside_avail_sok'] else 0
        inside_happymeal_layout_score = 1 if item['inside_happymeal_layout'] else 0
        inside_sok_layout_score = 1 if item['inside_sok_layout'] else 0

        employee_no=item['employee_no']
        inside_trans_id=item['inside_trans_id']
        inside_entry_campaigns=item['inside_entry_campaigns']
        inside_entry_campaigns_list=item['inside_entry_campaigns_list']
        inside_music=item['inside_music']
        inside_television=item['inside_television']
        inside_television_number=item['inside_television_number']
        inside_television_number_work=item['inside_television_number_work']
        inside_sok_layout=item['inside_sok_layout']
        inside_sok_layout_desc=item['inside_sok_layout_desc']
        inside_sok_campaigns_list=item['inside_sok_campaigns_list']
        inside_mystore_campaigns=item['inside_mystore_campaigns']
        inside_mystore_image_url=item['inside_mystore_image_url']
        inside_happymeal_layout=item['inside_happymeal_layout']
        inside_happymeal_layout_desc=item['inside_happymeal_layout_desc']
        inside_happymeal_campaigns_list=item['inside_happymeal_campaigns_list']
        inside_description=item['inside_description']
        inside_date=item['inside_date']
        inside_avail_sok=item['inside_avail_sok']
        inside_avail_sok_desc=item['inside_avail_sok_desc']
        store_id=item['store_id']
        site_name_store=Store_level.objects.filter(store_id=store_id).values('site_name')
        selected_store_name_store= site_name_store[0]['site_name'] if site_name_store else None
        out_store_site_name=selected_store_name_store
        total_score_inside += inside_music_score+inside_sok_layout_score+inside_happymeal_layout_score+inside_avail_sok_score
    else:
        print("No records found within the specified date range.")

    Mainqueryset = Menu.objects.filter(store_id=selected_store,menu_date__gte=start_date,menu_date__lte=end_date).values(
    'employee_no',
    'store_id',
    'menu_display',
    'menu_pop_layout',
    'menu_pop_layout_desc',
    'menu_pricepoint',
    'menu_board_display',
    'menu_board_display_desc',
    'menu_board_campaign_layout',
    'menu_board_campaign_layout_desc',
    'menu_board_campaig_list',
    'menu_trans_id',
    'menu_date',
    'menu_id').last()

    if Mainqueryset:
        item=Mainqueryset
        menu_pop_layout_score = 1 if item['menu_pop_layout'] else 0
        menu_board_display_score = 1 if item['menu_board_display'] else 0
        menu_board_campaign_layout_score = 1 if item['menu_board_campaign_layout'] else 0
        menu_display=item['menu_display']
        menu_pop_layout=item['menu_pop_layout']
        menu_pop_layout_desc=item['menu_pop_layout_desc']
        menu_pricepoint=item['menu_pricepoint']
        menu_board_display=item['menu_board_display']
        menu_board_display_desc=item['menu_board_display_desc']
        menu_board_campaign_layout=item['menu_board_campaign_layout']
        menu_board_campaig_list=item['menu_board_campaig_list']
        menu_board_campaign_layout_desc=item['menu_board_campaign_layout_desc']
        menu_date=item['menu_date']
        description_menu_store_site_name=selected_store_name
        total_score_Main += menu_pop_layout_score+menu_board_display_score+menu_board_campaign_layout_score
    else:
        print("No records found within the specified date range.")

    Mccafequeryset = McCafe.objects.filter(store_id=selected_store,mccafe_date__gte=start_date,mccafe_date__lte=end_date).values(
    'mccafe_id',
    'employee_no',
    'store_id',
    'mccafe_trans_id',
    'mccafe_menu',
    'mccafe_model',
    'mccafe_menu_display',
    'mccafe_menu_display_desc',
    'mccafe_menu_board_campaign_layout',
    'mccafe_menu_board_campaign_layout_desc',
    'mccafe_menu_board_layout_campaign_list',
    'mccafe_date').last()

    if Mccafequeryset:
        item=Mccafequeryset
        mccafe_menu_display_score = 1 if item['mccafe_menu_display'] else 0
        mccafe_menu_board_campaign_layout_score = 1 if item['mccafe_menu_board_campaign_layout'] else 0

        mccafe_id=item['mccafe_id']
        employee_no=item['employee_no']
        store_id=item['store_id']
        mccafe_trans_id=item['mccafe_trans_id']
        mccafe_menu=item['mccafe_menu']
        mccafe_model=item['mccafe_model']
        mccafe_menu_display=item['mccafe_menu_display']
        mccafe_menu_display_desc=item['mccafe_menu_display_desc']
        mccafe_menu_board_campaign_layout=item['mccafe_menu_board_campaign_layout']
        mccafe_menu_board_campaign_layout_desc=item['mccafe_menu_board_campaign_layout_desc']
        mccafe_menu_board_layout_campaign_list=item['mccafe_menu_board_layout_campaign_list']
        mccafe_date=item['mccafe_date']
        site_name_store=Store_level.objects.filter(store_id=store_id).values('site_name')
        selected_store_name_store= site_name_store[0]['site_name'] if site_name_store else None
        mccafe_store_site_name=selected_store_name_store
        total_score_Mccafe += mccafe_menu_display_score+mccafe_menu_board_campaign_layout_score
    else:
        print("No records found within the specified date range.")

    drivethruqueryset = Drivethru.objects.filter(store_id=selected_store,drivethru_date__gte=start_date,drivethru_date__lte=end_date).values(
    'employee_no',
    'store_id',
    'is_drivethru',
    'drive_menu',
    'drive_menu_board',
    'drive_menu_board_desc',
    'drive_menu_board_campaign_layout',
    'drive_menu_board_campaign_layout_desc',
    'drive_menu_board_layout_campaign_list',
    'drive_cod_layout',
    'drive_cod_layout_desc',
    'drive_advert',
    'drive_advert_desc',
    'drive_trans_id',
    'drivethru_date',
    'drivethru_id').last()
    if drivethruqueryset:
        item=drivethruqueryset
        drive_menu_board_campaign_layout_score = 1 if item['drive_menu_board_campaign_layout'] else 0
        drive_menu_board_score = 1 if item['drive_menu_board'] else 0
        drive_cod_layout_score = 1 if item['drive_cod_layout'] else 0

        drive_menu_board_layout_campaign_list=item['drive_menu_board_layout_campaign_list']
        drive_menu_board_campaign_layout_desc=item['drive_menu_board_campaign_layout_desc']
        drive_menu_board_campaign_layout=item['drive_menu_board_campaign_layout']
        drive_menu_board_desc=item['drive_menu_board_desc']
        drive_menu_board=item['drive_menu_board']
        drive_menu=item['drive_menu']
        is_drivethru=item['is_drivethru']
        store_id=item['store_id']
        employee_no=item['employee_no']
        drive_cod_layout=item['drive_cod_layout']
        drive_cod_layout_desc=item['drive_cod_layout_desc']
        drive_advert=item['drive_advert']
        drive_advert_desc=item['drive_advert_desc']
        drive_trans_id=item['drive_trans_id']
        drivethru_date=item['drivethru_date']
        drivethru_id=item['drivethru_id']
        store_id=item['store_id']
        site_name_store=Store_level.objects.filter(store_id=store_id).values('site_name')
        selected_store_name_store= site_name_store[0]['site_name'] if site_name_store else None
        drive_store_site_name=selected_store_name_store
        total_score_drivethru += drive_menu_board_campaign_layout_score+drive_menu_board_score+drive_cod_layout_score
    else:
        print("No records found within the specified date range.")

    deliveryqueryset = Delivery.objects.filter(store_id=selected_store,delivery_date__gte=start_date,delivery_date__lte=end_date).values(
    'employee_no',
    'store_id',
    'mcdelivery',
    'drive_other',
    'drive_other_desc',
    'del_trans_id',
    'delivery_date',
    'delivery_id').last()

    if deliveryqueryset:
        item=deliveryqueryset
        mcdelivery_score = 1 if item['mcdelivery'] else 0
        drive_other_score = 1 if item['drive_other'] else 0

        
        store_id=item['store_id']
        employee_no=item['employee_no']
        mcdelivery=item['mcdelivery']
        drive_other=item['drive_other']
        drive_other_desc=item['drive_other_desc']
        del_trans_id=item['del_trans_id']
        delivery_date=item['delivery_date']
        delivery_id=item['delivery_id']
        site_name_store=Store_level.objects.filter(store_id=store_id).values('site_name')
        selected_store_name_store= site_name_store[0]['site_name'] if site_name_store else None
        store_site_name=selected_store_name_store
        total_score_delivery += drive_other_score+mcdelivery_score
                    
    data.append({'drive_other':drive_other,'mcdelivery':mcdelivery,'drive_advert_desc':drive_advert_desc,'drive_advert':drive_advert,'drive_cod_layout_desc':drive_cod_layout_desc,'drive_cod_layout':drive_cod_layout,'drive_menu_board_layout_campaign_list':drive_menu_board_layout_campaign_list,'drive_menu_board_campaign_layout_desc':drive_menu_board_campaign_layout_desc,'drive_menu_board_campaign_layout':drive_menu_board_campaign_layout,'drive_menu_board_desc':drive_menu_board_desc,'drive_menu_board':drive_menu_board,'drive_menu':drive_menu,'is_drivethru':is_drivethru,'mccafe_menu_board_layout_campaign_list':mccafe_menu_board_layout_campaign_list,'mccafe_menu_board_campaign_layout_desc':mccafe_menu_board_campaign_layout_desc,'mccafe_menu_board_campaign_layout':mccafe_menu_board_campaign_layout,'mccafe_menu_display_desc':mccafe_menu_display_desc,'mccafe_menu_display':mccafe_menu_display,'mccafe_menu':mccafe_menu,'mccafe_model':mccafe_model,'menu_board_campaig_list':menu_board_campaig_list,'menu_board_campaign_layout_desc':menu_board_campaign_layout_desc,'menu_board_campaign_layout':menu_board_campaign_layout,'menu_board_display_desc':menu_board_display_desc,'menu_board_display':menu_board_display,'menu_pricepoint':menu_pricepoint,'menu_display':menu_display,'menu_pop_layout_desc':menu_pop_layout_desc,'menu_pop_layout':menu_pop_layout,'menu_date':menu_date,'inside_happymeal_campaigns_list':inside_happymeal_campaigns_list,'inside_happymeal_layout_desc':inside_happymeal_layout_desc,'inside_happymeal_layout':inside_happymeal_layout,'inside_mystore_image_url':inside_mystore_image_url,'inside_mystore_campaigns':inside_mystore_campaigns,'inside_sok_campaigns_list':inside_sok_campaigns_list,'inside_sok_layout_desc':inside_sok_layout_desc,'inside_sok_layout':inside_sok_layout,'inside_avail_sok':inside_avail_sok,'inside_television_number_work':inside_television_number_work,'inside_television_number':inside_television_number,'inside_television':inside_television,'inside_music':inside_music,'inside_entry_campaigns_list':inside_entry_campaigns_list,'inside_entry_campaigns':inside_entry_campaigns,'inside_date':inside_date,'outside_image_url':outside_image_url,'outside_promotions':outside_promotions,'outside_promotions_desc':outside_promotions_desc,'out_pop_description_inside':out_pop_description_inside,'mystorecamp_img_url':mystorecamp_img_url,'digital_menu_mc':digital_menu_mc,'insidemystorecamp':insidemystorecamp,'outsidemystorecamp':outsidemystorecamp,'digital_menu':digital_menu,'out_campaign_outside_store_site_name':out_campaign_outside_store_site_name,'out_campaign_outside_date':out_campaign_outside_date,'out_store_site_name':out_store_site_name,'out_description_inside_date':out_description_inside_date,'description_menu_store_site_name':description_menu_store_site_name,'description_menu_date':description_menu_date,'mccafe_store_site_name':mccafe_store_site_name,'mccafe_date':mccafe_date,'drive_store_site_name':drive_store_site_name,'drivethru_date':drivethru_date,'store_site_name':store_site_name,'delivery_date':delivery_date,'description_delivery':description_delivery,'target_delivery':target_delivery,'third_party_del':third_party_del,'mc_delivery':mc_delivery,'total_score_delivery':total_score_delivery,'activation_description':activation_description,'customer_order_display':customer_order_display,'drivethru_campaign':drivethru_campaign,'target_drivethru':target_drivethru,'activation_on_promo':activation_on_promo,'total_score_drivethru':total_score_drivethru,'description_mccafe':description_mccafe,'menu_promo':menu_promo,'mccafemenu_visibility':mccafemenu_visibility,'target_mccafe':target_mccafe,'total_score_Mccafe':total_score_Mccafe,'description_menu':description_menu,'menu_promotion':menu_promotion,'price_visibility':price_visibility,'out_description_inside':out_description_inside,'out_happy_m_campaign':out_happy_m_campaign,'out_promo_sok_campaigns':out_promo_sok_campaigns,'out_description_outside':out_description_outside,'out_campaigns':out_campaigns,'total_score_Main': total_score_Main,'menu_visibility':menu_visibility,'target_menu':target_menu,'total_score_inside': total_score_inside,'out_point_of_sale':out_point_of_sale,'out_self_order_kiosk':out_self_order_kiosk,'target_inside':target_inside,'total_score_outside': total_score_outside,'out_campaign':out_campaign, 'target_outside': target_outside, 'selected_store': selected_store,'out_branding_condition':out_branding_condition,'out_signage_condition':out_signage_condition})
    return JsonResponse(data, safe=False)

