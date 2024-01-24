from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import Province,Store_Map,StorePerformance,Shops as Store_level,Inside,Outside,Menu,Mccafe as McCafe,Drivethru as Drivethru,Delivery as Delivery # Import the Province model
from django.http import JsonResponse
import random
import calendar
from django.views import View
from datetime import datetime
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.timezone import make_aware


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

@login_required()
def home_view(request):
    provinces = Province.objects.all()  # Retrieve all provinces from the database
    user = request.user
    username=user.username
    region_name = Store_level.objects.values('region').distinct()
    franchise_mcopco = Store_level.objects.values('portfolio_type').distinct()
    ids=Menu.objects.values('store_id')
    #restaurant= Store_level.objects.values('site_name').distinct()
    restaurant= Store_level.objects.filter(store_id__in=ids).values('site_name','store_id')
    print('store_ids')
    print(restaurant)
    context = {'provinces': provinces,'username':username,'franchise_mcopco':franchise_mcopco,'restaurant':restaurant,'region_name':region_name}
    return render(request, 'home.html', context)

@login_required()
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to your login page

@login_required()   
def get_store_data(request):
    selected_province = request.GET.get('province', 'all')

    try:
        data = []  # Initialize the data list
        if selected_province == 'all':
            stores = Store_level.objects.values('site_name', 'latitude', 'longitude', 'region')
        else:
            stores = Store_level.objects.filter(province=selected_province).values('site_name', 'latitude', 'longitude', 'region')

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
    #selected_stire_franchise = request.GET.get('owner_franchise', 'all')
    selected_store = request.GET.get('store', 'all')
    #selected_store=1
    site_name=Store_level.objects.filter(store_id=selected_store).values('site_name')
    selected_store_name= site_name[0]['site_name'] if site_name else None
    print(selected_store)
    
    
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
    target_mccafe = 1
    target_delivery = 2
    target_drivethru = 1
    target_inside=3
    target_menu=1
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
    digital_menu_mc=0
    Outqueryset = Outside.objects.filter(
        store_id=selected_store,
        outside_date__gte=start_date,
        outside_date__lte=end_date
    ).values(
        'store_id',
        'employee_no',
        'outside_date',
        'outsidemystorecamp',
        'disclaimer',
        'campaigns',
        'campaigns_list',
        'description_outside',
        'signage_condition'
    ).last()
    print('OutSide')
    print(Outqueryset)

    if Outqueryset:
        item = Outqueryset  # No need to loop, as there's only one record

        branding_condition_score = 1 if item['signage_condition'] else 0
        signage_condition_score = 1 if item['disclaimer'] else 0
        campaign_score = 1 if item['campaigns'] else 0
        outsidemystorecamp_score = 1 if item['outsidemystorecamp'] else 0

        out_branding_condition = item['signage_condition']
        out_signage_condition = item['disclaimer']
        out_campaigns = item['campaigns_list']
        outsidemystorecamp=item['outsidemystorecamp']
        out_description_outside = item['description_outside']
        out_campaign = item['campaigns']
        out_campaign_outside_date = item['outside_date']
        store_id = item['store_id']
        site_name_store = Store_level.objects.filter(store_id=store_id).values('site_name')
        print('Campaigns')
        print(out_campaigns)
        selected_store_name_store = site_name_store[0]['site_name'] if site_name_store else None
        out_campaign_outside_store_site_name = selected_store_name_store
        total_score_outside += branding_condition_score + signage_condition_score + campaign_score+outsidemystorecamp_score
    else:
        print("No records found within the specified date range.")


    Inqueryset = Inside.objects.filter(store_id=selected_store,inside_date__gte=start_date,inside_date__lte=end_date).values('insidemystorecamp','store_id','pop_description','employee_no','inside_date', 'point_of_purchase','self_order_kiosk','promo_sok_campaigns_list','happy_m_campaign','description_inside').last()
    print('Inside')
    print(Inqueryset)
    if Inqueryset:
        item =Inqueryset
        point_of_sale_score = 1 if item['point_of_purchase'] else 0
        self_order_kiosk_score = 1 if item['self_order_kiosk'] else 0
        insidemystorecamp_score = 1 if item['insidemystorecamp'] else 0

        out_point_of_sale=item['point_of_purchase']
        out_self_order_kiosk=item['self_order_kiosk']
        out_promo_sok_campaigns=item['promo_sok_campaigns_list']
        out_happy_m_campaign=item['happy_m_campaign']
        out_description_inside=item['description_inside']
        out_description_inside_date=item['inside_date']
        insidemystorecamp=item['insidemystorecamp']
        store_id=item['store_id']
        site_name_store=Store_level.objects.filter(store_id=store_id).values('site_name')
        selected_store_name_store= site_name_store[0]['site_name'] if site_name_store else None
        out_store_site_name=selected_store_name_store
        out_pop_description_inside=item['pop_description']
        total_score_inside += point_of_sale_score + self_order_kiosk_score+insidemystorecamp_score
    else:
        print("No records found within the specified date range.")

    Mainqueryset = Menu.objects.filter(store_id=selected_store,menu_date__gte=start_date,menu_date__lte=end_date).values('digital_menu','store_id','employee_no', 'menu_visibility','price_visibility','menu_promotion','description_menu','menu_date').last()
    print('Main')
    print(Mainqueryset)
    if Mainqueryset:
        item=Mainqueryset
        menu_visibility_score = 1 if item['menu_visibility'] else 0

        menu_visibility=item['menu_visibility']
        price_visibility=item['price_visibility']
        menu_promotion=item['menu_promotion']
        description_menu=item['description_menu']
        description_menu_date=item['menu_date']
        digital_menu=item['digital_menu']
        description_menu_store_site_name=selected_store_name
        total_score_Main += menu_visibility_score
    else:
        print("No records found within the specified date range.")

    Mccafequeryset = McCafe.objects.filter(store_id=selected_store,mccafe_date__gte=start_date,mccafe_date__lte=end_date).values('digital_menu_mc','store_id','employee_no',  'menu_visibility','description_mccafe','description_mccafe','mccafe_date').last()
    print('McCafe')
    print(Mccafequeryset)
    if Mccafequeryset:
        item=Mccafequeryset
        mccafemenu_visibility_score = 1 if item['menu_visibility'] else 0

        mccafemenu_visibility=item['menu_visibility']
        menu_promo=item['description_mccafe']
        description_mccafe=item['description_mccafe']
        mccafe_date=item['mccafe_date']
        store_id=item['store_id']
        digital_menu_mc=item['digital_menu_mc']
        site_name_store=Store_level.objects.filter(store_id=store_id).values('site_name')
        selected_store_name_store= site_name_store[0]['site_name'] if site_name_store else None
        mccafe_store_site_name=selected_store_name_store
        total_score_Mccafe += mccafemenu_visibility_score
    else:
        print("No records found within the specified date range.")

    drivethruqueryset = Drivethru.objects.filter(store_id=selected_store,drivethru_date__gte=start_date,drivethru_date__lte=end_date).values('store_id','employee_no', 'activation_on_promo','drivethru_campaign','customer_order_display','activation_description','drivethru_date').last()
    print('Drive')
    print(drivethruqueryset)
    if drivethruqueryset:
        item=drivethruqueryset
        activation_on_promo_score = 1 if item['activation_on_promo'] else 0

        activation_on_promo=item['activation_on_promo']
        drivethru_campaign=item['drivethru_campaign']
        customer_order_display=item['customer_order_display']
        activation_description=item['activation_description']
        drivethru_date=item['drivethru_date']
        store_id=item['store_id']
        site_name_store=Store_level.objects.filter(store_id=store_id).values('site_name')
        selected_store_name_store= site_name_store[0]['site_name'] if site_name_store else None
        drive_store_site_name=selected_store_name_store
        total_score_drivethru += activation_on_promo_score
    else:
        print("No records found within the specified date range.")

    deliveryqueryset = Delivery.objects.filter(store_id=selected_store,delivery_date__gte=start_date,delivery_date__lte=end_date).values('store_id','employee_no','mcdelivery','third_party_del','description_delivery','delivery_date').last()
    print('Dilivery')
    print(deliveryqueryset)
    if deliveryqueryset:
        item=deliveryqueryset
        mc_delivery_score = 1 if item['mcdelivery'] else 0
        third_party_del_score = 1 if item['third_party_del'] else 0

        mc_delivery=item['mcdelivery']
        third_party_del=item['third_party_del']
        description_delivery=item['description_delivery']
        delivery_date=item['delivery_date']
        store_id=item['store_id']
        site_name_store=Store_level.objects.filter(store_id=store_id).values('site_name')
        selected_store_name_store= site_name_store[0]['site_name'] if site_name_store else None
        store_site_name=selected_store_name_store
        total_score_delivery += mc_delivery_score+third_party_del_score
                    
    data.append({'out_pop_description_inside':out_pop_description_inside,'digital_menu_mc':digital_menu_mc,'insidemystorecamp':insidemystorecamp,'outsidemystorecamp':outsidemystorecamp,'digital_menu':digital_menu,'out_campaign_outside_store_site_name':out_campaign_outside_store_site_name,'out_campaign_outside_date':out_campaign_outside_date,'out_store_site_name':out_store_site_name,'out_description_inside_date':out_description_inside_date,'description_menu_store_site_name':description_menu_store_site_name,'description_menu_date':description_menu_date,'mccafe_store_site_name':mccafe_store_site_name,'mccafe_date':mccafe_date,'drive_store_site_name':drive_store_site_name,'drivethru_date':drivethru_date,'store_site_name':store_site_name,'delivery_date':delivery_date,'description_delivery':description_delivery,'target_delivery':target_delivery,'third_party_del':third_party_del,'mc_delivery':mc_delivery,'total_score_delivery':total_score_delivery,'activation_description':activation_description,'customer_order_display':customer_order_display,'drivethru_campaign':drivethru_campaign,'target_drivethru':target_drivethru,'activation_on_promo':activation_on_promo,'total_score_drivethru':total_score_drivethru,'description_mccafe':description_mccafe,'menu_promo':menu_promo,'mccafemenu_visibility':mccafemenu_visibility,'target_mccafe':target_mccafe,'total_score_Mccafe':total_score_Mccafe,'description_menu':description_menu,'menu_promotion':menu_promotion,'price_visibility':price_visibility,'out_description_inside':out_description_inside,'out_happy_m_campaign':out_happy_m_campaign,'out_promo_sok_campaigns':out_promo_sok_campaigns,'out_description_outside':out_description_outside,'out_campaigns':out_campaigns,'total_score_Main': total_score_Main,'menu_visibility':menu_visibility,'target_menu':target_menu,'total_score_inside': total_score_inside,'out_point_of_sale':out_point_of_sale,'out_self_order_kiosk':out_self_order_kiosk,'target_inside':target_inside,'total_score_outside': total_score_outside,'out_campaign':out_campaign, 'target_outside': target_outside, 'selected_store': selected_store,'out_branding_condition':out_branding_condition,'out_signage_condition':out_signage_condition})
    print(data)
    return JsonResponse(data, safe=False)
