from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import Province,Store_Map,EntranceEvaluation,StorePerformance,Store_level,Inside,Outside,Menu,McCafe,Drivethru,Delivery # Import the Province model
from django.http import JsonResponse
import random
from django.views import View
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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
    region_name = Store_level.objects.values('region__name').distinct()
    franchise_mcopco = Store_level.objects.values('franchise_mcopco').distinct()
    restaurant= Store_level.objects.values('restaurant').distinct()
    restaurant= Store_level.objects.values('restaurant').distinct()
    context = {'provinces': provinces,'username':username,'franchise_mcopco':franchise_mcopco,'restaurant':restaurant,'region_name':region_name}
    return render(request, 'home.html', context)

@login_required()
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to your login page

@login_required()   
def get_store_data(request):
    # Get the selected province from the request's GET parameters
    selected_province = request.GET.get('province', 'all')
    # Retrieve store data based on the selected province
    if selected_province == 'all':
        stores = Store_Map.objects.values('name', 'lat', 'lon', 'province')
        performance_data = StorePerformance.objects.values('store__name', 'target', 'achieved')
    else:
        stores = Store_Map.objects.filter(province=selected_province).values('name', 'lat', 'lon', 'province')
        performance_data = StorePerformance.objects.filter(store__province=selected_province).values('store__name', 'target', 'achieved')

    # Combine store and performance data
    data = []
    for store in stores:
        store_performance = next((perf for perf in performance_data if perf['store__name'] == store['name']), None)
        if store_performance:
            store.update(store_performance)
        data.append(store)
    

    # Retrieve store data based on the selected province
    if selected_province == 'all':
        stores = Store_Map.objects.values('name', 'lat', 'lon', 'province')
        performance_data = StorePerformance.objects.values('store__name', 'target', 'achieved')
    else:
        stores = Store_Map.objects.filter(province=selected_province).values('name', 'lat', 'lon', 'province')
        performance_data = StorePerformance.objects.filter(store__province=selected_province).values('store__name', 'target', 'achieved')

    # Combine store and performance data
    total_score_outside = 0  # Initialize total_score_outside outside the loop
    target_score_inside=2*Inside.objects.count()
    target_score_Mccafe=1*McCafe.objects.count()
    target_score_delivery=2*Delivery.objects.count()
    target_score_drivethru=1*Drivethru.objects.count()
    target_outside = 3*Outside.objects.count()
    target_score_Main=1*Menu.objects.count()
    out_branding_condition = 0  # Initialize out_branding_condition
    out_signage_condition = 0  # Initialize out_signage_condition
    out_campaign = 0  # Initialize out_campaign
    total_score_inside=0
    total_score_Main=0
    total_score_Mccafe=0
    total_score_drivethru=0
    total_score_delivery=0
    if selected_province == 'all':
        Outqueryset = Outside.objects.select_related('store').values('employee_no', 'store__site_name', 'branding_condition', 'signage_condition', 'campaign')
        for item in Outqueryset:
            branding_condition_score = 1 if item['branding_condition'] else 0
            signage_condition_score = 1 if item['signage_condition'] else 0
            campaign_score = 1 if item['campaign'] else 0

            out_branding_condition=item['branding_condition']
            out_signage_condition=item['signage_condition']
            out_campaign=item['campaign']
            total_score_outside += branding_condition_score + signage_condition_score + campaign_score
        Inqueryset = Inside.objects.select_related('store').values('employee_no', 'store__site_name', 'point_of_sale','self_order_kiosk','promo_sok_campaigns','happy_m_campaign','description_inside')
        for item in Inqueryset:
            point_of_sale_score = 1 if item['point_of_sale'] else 0
            self_order_kiosk_score = 1 if item['self_order_kiosk'] else 0

            out_point_of_sale=item['point_of_sale']
            out_self_order_kiosk=item['self_order_kiosk']
            out_promo_sok_campaigns=item['promo_sok_campaigns']
            out_happy_m_campaign=item['happy_m_campaign']
            out_description_inside=item['description_inside']
            total_score_inside += point_of_sale_score + self_order_kiosk_score

        Mainqueryset = Menu.objects.select_related('store').values('employee_no', 'store__site_name', 'menu_visibility','price_visibility','menu_promotion','description_menu')
        for item in Mainqueryset:
            menu_visibility_score = 1 if item['menu_visibility'] else 0

            menu_visibility=item['menu_visibility']
            price_visibility=item['price_visibility']
            menu_promotion=item['menu_promotion']
            description_menu=item['description_menu']
            total_score_Main += menu_visibility_score
        Mccafequeryset = McCafe.objects.select_related('store').values('employee_no', 'store__site_name', 'menu_visibility','menu_promo','description_mccafe')
        for item in Mccafequeryset:
            mccafemenu_visibility_score = 1 if item['menu_visibility'] else 0

            mccafemenu_visibility=item['menu_visibility']
            menu_promo=item['menu_promo']
            description_mccafe=item['description_mccafe']
            total_score_Mccafe += mccafemenu_visibility_score

        Mccafequeryset = McCafe.objects.select_related('store').values('employee_no', 'store__site_name', 'menu_visibility','menu_promo','description_mccafe')
        for item in Mccafequeryset:
            mccafemenu_visibility_score = 1 if item['menu_visibility'] else 0

            mccafemenu_visibility=item['menu_visibility']
            menu_promo=item['menu_promo']
            description_mccafe=item['description_mccafe']
            total_score_Mccafe += mccafemenu_visibility_score

        drivethruqueryset = Drivethru.objects.select_related('store').values('employee_no', 'store__site_name', 'activation_on_promo','drivethru_campaign','customer_order_display','activation_description')
        
        for item in drivethruqueryset:
            activation_on_promo_score = 1 if item['activation_on_promo'] else 0

            activation_on_promo=item['activation_on_promo']
            drivethru_campaign=item['drivethru_campaign']
            customer_order_display=item['customer_order_display']
            activation_description=item['activation_description']
            total_score_drivethru += activation_on_promo_score

        deliveryqueryset = Delivery.objects.select_related('store').values('employee_no', 'store__site_name','mc_delivery','third_party_del','description_delivery')
        for item in deliveryqueryset:
            mc_delivery_score = 1 if item['mc_delivery'] else 0
            third_party_del_score = 1 if item['third_party_del'] else 0

            mc_delivery=item['mc_delivery']
            third_party_del=item['third_party_del']
            description_delivery=item['description_delivery']
            total_score_delivery += mc_delivery_score+third_party_del_score

        data.append({'target_score_delivery':target_score_delivery,'total_score_delivery':total_score_delivery,'target_score_drivethru':target_score_drivethru,'total_score_drivethru':total_score_drivethru,'target_score_Mccafe':target_score_Mccafe,'total_score_Mccafe':total_score_Mccafe,'target_score_Main':target_score_Main,'total_score_Main':total_score_Main,'target_score_inside':target_score_inside,'total_score_inside':total_score_inside,'target_inside': total_score_outside,'target_output_inside':target_outside,'target': target_outside, 'target_output': total_score_outside,'selected_province':selected_province})
    else:
        Outqueryset1 = Outside.objects.select_related('store').values('employee_no', 'store__site_name', 'branding_condition', 'signage_condition', 'campaign')
        Outqueryset = Outqueryset1.filter(store__region__name=selected_province)
        for item in Outqueryset:
            branding_condition_score = 1 if item['branding_condition'] else 0
            signage_condition_score = 1 if item['signage_condition'] else 0
            campaign_score = 1 if item['campaign'] else 0

            out_branding_condition=item['branding_condition']
            out_signage_condition=item['signage_condition']
            out_campaign=item['campaign']
            total_score_outside += branding_condition_score + signage_condition_score + campaign_score

        Inqueryset = Inside.objects.select_related('store').values('employee_no', 'store__site_name', 'point_of_sale','self_order_kiosk','promo_sok_campaigns','happy_m_campaign','description_inside')
        Inqueryset = Inqueryset.filter(store__region__name=selected_province)
        for item in Inqueryset:
            point_of_sale_score = 1 if item['point_of_sale'] else 0
            self_order_kiosk_score = 1 if item['self_order_kiosk'] else 0

            out_point_of_sale=item['point_of_sale']
            out_self_order_kiosk=item['self_order_kiosk']
            out_promo_sok_campaigns=item['promo_sok_campaigns']
            out_happy_m_campaign=item['happy_m_campaign']
            out_description_inside=item['description_inside']
            total_score_inside += point_of_sale_score + self_order_kiosk_score

        Mainqueryset = Menu.objects.select_related('store').values('employee_no', 'store__site_name', 'menu_visibility','price_visibility','menu_promotion','description_menu')
        Mainqueryset = Mainqueryset.filter(store__region__name=selected_province)
        for item in Mainqueryset:
            menu_visibility_score = 1 if item['menu_visibility'] else 0

            menu_visibility=item['menu_visibility']
            price_visibility=item['price_visibility']
            menu_promotion=item['menu_promotion']
            description_menu=item['description_menu']
            total_score_Main += menu_visibility_score
        Mccafequeryset = McCafe.objects.select_related('store').values('employee_no', 'store__site_name', 'menu_visibility','menu_promo','description_mccafe')
        Mccafequeryset = Mccafequeryset.filter(store__region__name=selected_province)
        for item in Mccafequeryset:
            mccafemenu_visibility_score = 1 if item['menu_visibility'] else 0

            mccafemenu_visibility=item['menu_visibility']
            menu_promo=item['menu_promo']
            description_mccafe=item['description_mccafe']
            total_score_Mccafe += mccafemenu_visibility_score
        drivethruqueryset = Drivethru.objects.select_related('store').values('employee_no', 'store__site_name', 'activation_on_promo','drivethru_campaign','customer_order_display','activation_description')
        drivethruqueryset = drivethruqueryset.filter(store__region__name=selected_province)
        for item in drivethruqueryset:
            activation_on_promo_score = 1 if item['activation_on_promo'] else 0

            activation_on_promo=item['activation_on_promo']
            drivethru_campaign=item['drivethru_campaign']
            customer_order_display=item['customer_order_display']
            activation_description=item['activation_description']
            total_score_drivethru += activation_on_promo_score

        deliveryqueryset = Delivery.objects.select_related('store').values('employee_no', 'store__site_name','mc_delivery','third_party_del','description_delivery')
        deliveryqueryset = deliveryqueryset.filter(store__region__name=selected_province)
        for item in deliveryqueryset:
            mc_delivery_score = 1 if item['mc_delivery'] else 0
            third_party_del_score = 1 if item['third_party_del'] else 0

            mc_delivery=item['mc_delivery']
            third_party_del=item['third_party_del']
            description_delivery=item['description_delivery']
            total_score_delivery += mc_delivery_score+third_party_del_score

        data.append({'target_score_delivery':target_score_delivery,'total_score_delivery':total_score_delivery,'target_score_drivethru':target_score_drivethru,'total_score_drivethru':total_score_drivethru,'target_score_Mccafe':target_score_Mccafe,'total_score_Mccafe':total_score_Mccafe,'target_score_Main':target_score_Main,'total_score_Main':total_score_Main,'target_score_inside':target_score_inside,'total_score_inside':total_score_inside,'target_inside': total_score_outside,'target_output_inside':target_outside,'target': target_outside, 'target_output': total_score_outside,'selected_province':selected_province})
    return JsonResponse(data, safe=False)

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

@login_required()
def get_store_data_store_level(request):
    selected_province_store = request.GET.get('province_store', 'all')
    selected_stire_franchise = request.GET.get('owner_franchise', 'all')
    selected_store = request.GET.get('store', 'all')
    from_date = request.GET.get('from_date', None)
    to_date = request.GET.get('to_date', None)
    
    data = []
    total_score_outside = 0 
    total_score_inside=0 # Initialize total_score_outside outside the loop
    total_score_Main=0
    target_outside = 3
    total_score_Mccafe=0
    target_mccafe = 1
    target_delivery = 2
    target_drivethru = 1
    target_inside=2
    target_menu=1
    out_branding_condition = 0  # Initialize out_branding_condition
    out_signage_condition = 0  # Initialize out_signage_condition
    out_point_of_sale=0
    out_self_order_kiosk=0
    menu_visibility=0
    out_campaign = 0  # Initialize out_campaign
    out_campaigns=0
    out_description_outside=0
    out_happy_m_campaign=0
    out_description_inside=0
    out_promo_sok_campaigns=0
    price_visibility=0
    menu_promotion=0
    description_menu=0
    mccafemenu_visibility_score=0
    mccafemenu_visibility=0
    menu_promo=0
    activation_on_promo=0
    description_mccafe=0
    total_score_drivethru=0
    drivethru_campaign=0
    customer_order_display=0
    activation_description=0
    total_score_delivery=0
    mc_delivery=0
    third_party_del=0
    description_delivery=0
    if selected_store == 'all':
        Outqueryset = Outside.objects.select_related('store').values('employee_no', 'store__site_name', 'branding_condition', 'signage_condition', 'campaign','campaigns','description_outside')
        Outqueryset = Outqueryset.filter(outside_date__range=[from_date, to_date])
        for item in Outqueryset:
            branding_condition_score = 1 if item['branding_condition'] else 0
            signage_condition_score = 1 if item['signage_condition'] else 0
            campaign_score = 1 if item['campaign'] else 0

            out_branding_condition=item['branding_condition']
            out_signage_condition=item['signage_condition']
            out_campaigns=item['campaigns']
            out_description_outside=item['description_outside']
            out_campaign=item['campaign']
            total_score_outside += branding_condition_score + signage_condition_score + campaign_score

        Inqueryset = Inside.objects.select_related('store').values('employee_no', 'store__site_name', 'point_of_sale','self_order_kiosk','promo_sok_campaigns','happy_m_campaign','description_inside')
        Inqueryset = Inqueryset.filter(inside_date__range=[from_date, to_date])
        for item in Inqueryset:
            point_of_sale_score = 1 if item['point_of_sale'] else 0
            self_order_kiosk_score = 1 if item['self_order_kiosk'] else 0

            out_point_of_sale=item['point_of_sale']
            out_self_order_kiosk=item['self_order_kiosk']
            out_promo_sok_campaigns=item['promo_sok_campaigns']
            out_happy_m_campaign=item['happy_m_campaign']
            out_description_inside=item['description_inside']
            total_score_inside += point_of_sale_score + self_order_kiosk_score

        Mainqueryset = Menu.objects.select_related('store').values('employee_no', 'store__site_name', 'menu_visibility','price_visibility','menu_promotion','description_menu')
        Mainqueryset = Mainqueryset.filter(menu_date__range=[from_date, to_date])
        for item in Mainqueryset:
            menu_visibility_score = 1 if item['menu_visibility'] else 0

            menu_visibility=item['menu_visibility']
            price_visibility=item['price_visibility']
            menu_promotion=item['menu_promotion']
            description_menu=item['description_menu']
            total_score_Main += menu_visibility_score
        
        Mccafequeryset = McCafe.objects.select_related('store').values('employee_no', 'store__site_name', 'menu_visibility','menu_promo','description_mccafe')
        Mccafequeryset = Mccafequeryset.filter(store__site_name=selected_store,mccafe_date__range=[from_date, to_date])
        for item in Mccafequeryset:
            mccafemenu_visibility_score = 1 if item['menu_visibility'] else 0

            mccafemenu_visibility=item['menu_visibility']
            menu_promo=item['menu_promo']
            description_mccafe=item['description_mccafe']
            total_score_Mccafe += mccafemenu_visibility_score
        
        drivethruqueryset = Drivethru.objects.select_related('store').values('employee_no', 'store__site_name', 'activation_on_promo','drivethru_campaign','customer_order_display','activation_description')
        drivethruqueryset = drivethruqueryset.filter(store__site_name=selected_store,mccafe_date__range=[from_date, to_date])
        for item in drivethruqueryset:
            activation_on_promo_score = 1 if item['activation_on_promo'] else 0

            activation_on_promo=item['activation_on_promo']
            drivethru_campaign=item['drivethru_campaign']
            customer_order_display=item['customer_order_display']
            activation_description=item['activation_description']
            total_score_drivethru += activation_on_promo_score

        deliveryqueryset = Deliveryobjects.select_related('store').values('employee_no', 'store__site_name','mc_delivery','third_party_del','description_delivery')
        deliveryqueryset = deliveryqueryset.filter(store__site_name=selected_store,delivery_date__range=[from_date, to_date])
        for item in deliveryqueryset:
            mc_delivery_score = 1 if item['mc_delivery'] else 0
            third_party_del_score = 1 if item['third_party_del'] else 0

            mc_delivery=item['mc_delivery']
            third_party_del=item['third_party_del']
            description_delivery=item['description_delivery']
            total_score_delivery += mc_delivery_score+third_party_del_score

        data.append({'description_delivery':description_delivery,'target_delivery':target_delivery,'third_party_del':third_party_del,'mc_delivery':mc_delivery,'total_score_delivery':total_score_delivery,'activation_description':activation_description,'customer_order_display':customer_order_display,'drivethru_campaign':drivethru_campaign,'target_drivethru':target_drivethru,'activation_on_promo':activation_on_promo,'total_score_drivethru':total_score_drivethru,'description_mccafe':description_mccafe,'menu_promo':menu_promo,'mccafemenu_visibility':mccafemenu_visibility,'target_mccafe':target_mccafe,'total_score_Mccafe':total_score_Mccafe,'description_menu':description_menu,'menu_promotion':menu_promotion,'price_visibility':price_visibility,'out_description_inside':out_description_inside,'out_happy_m_campaign':out_happy_m_campaign,'out_promo_sok_campaigns':out_promo_sok_campaigns,'out_description_outside':out_description_outside,'out_campaigns':out_campaigns,'total_score_Main': total_score_Main,'menu_visibility':menu_visibility,'target_menu':target_menu,'total_score_inside': total_score_inside,'out_point_of_sale':out_point_of_sale,'out_self_order_kiosk':out_self_order_kiosk,'target_inside':target_inside,'total_score_outside': total_score_outside,'out_campaign':out_campaign, 'target_outside': target_outside, 'selected_store': selected_store,'out_branding_condition':out_branding_condition,'out_signage_condition':out_signage_condition})
    else:
        Outqueryset1 = Outside.objects.select_related('store').values('employee_no','outside_date' ,'store__site_name', 'branding_condition', 'signage_condition', 'campaign','campaigns','description_outside')
        Outqueryset = Outqueryset1.filter(store__site_name=selected_store, outside_date__range=[from_date, to_date])
        for item in Outqueryset:
            branding_condition_score = 1 if item['branding_condition'] else 0
            signage_condition_score = 1 if item['signage_condition'] else 0
            campaign_score = 1 if item['campaign'] else 0

            out_branding_condition=item['branding_condition']
            out_signage_condition=item['signage_condition']
            out_campaigns=item['campaigns']
            out_description_outside=item['description_outside']
            out_campaign=item['campaign']
            out_campaign_outside_date=item['outside_date']
            out_campaign_outside_store_site_name=item['store__site_name']
            total_score_outside += branding_condition_score + signage_condition_score + campaign_score

        Inqueryset = Inside.objects.select_related('store').values('employee_no','inside_date','store__site_name', 'point_of_sale','self_order_kiosk','promo_sok_campaigns','happy_m_campaign','description_inside')
        Inqueryset = Inqueryset.filter(store__site_name=selected_store,inside_date__range=[from_date, to_date])
        for item in Inqueryset:
            point_of_sale_score = 1 if item['point_of_sale'] else 0
            self_order_kiosk_score = 1 if item['self_order_kiosk'] else 0

            out_point_of_sale=item['point_of_sale']
            out_self_order_kiosk=item['self_order_kiosk']
            out_promo_sok_campaigns=item['promo_sok_campaigns']
            out_happy_m_campaign=item['happy_m_campaign']
            out_description_inside=item['description_inside']
            out_description_inside_date=item['inside_date']
            out_store_site_name=item['store__site_name']
            total_score_inside += point_of_sale_score + self_order_kiosk_score

        Mainqueryset = Menu.objects.select_related('store').values('employee_no', 'store__site_name', 'menu_visibility','price_visibility','menu_promotion','description_menu','menu_date')
        Mainqueryset = Mainqueryset.filter(store__site_name=selected_store,menu_date__range=[from_date, to_date])
        for item in Mainqueryset:
            menu_visibility_score = 1 if item['menu_visibility'] else 0

            menu_visibility=item['menu_visibility']
            price_visibility=item['price_visibility']
            menu_promotion=item['menu_promotion']
            description_menu=item['description_menu']
            description_menu_date=item['menu_date']
            description_menu_store_site_name=item['store__site_name']
            total_score_Main += menu_visibility_score

        Mccafequeryset = McCafe.objects.select_related('store').values('employee_no', 'store__site_name', 'menu_visibility','menu_promo','description_mccafe','mccafe_date')
        Mccafequeryset = Mccafequeryset.filter(store__site_name=selected_store,mccafe_date__range=[from_date, to_date])
        for item in Mccafequeryset:
            mccafemenu_visibility_score = 1 if item['menu_visibility'] else 0

            mccafemenu_visibility=item['menu_visibility']
            menu_promo=item['menu_promo']
            description_mccafe=item['description_mccafe']
            mccafe_date=item['mccafe_date']
            mccafe_store_site_name=item['store__site_name']
            total_score_Mccafe += mccafemenu_visibility_score

        drivethruqueryset = Drivethru.objects.select_related('store').values('employee_no', 'store__site_name', 'activation_on_promo','drivethru_campaign','customer_order_display','activation_description','drivethru_date')
        drivethruqueryset = drivethruqueryset.filter(store__site_name=selected_store,drivethru_date__range=[from_date, to_date])
        for item in drivethruqueryset:
            activation_on_promo_score = 1 if item['activation_on_promo'] else 0

            activation_on_promo=item['activation_on_promo']
            drivethru_campaign=item['drivethru_campaign']
            customer_order_display=item['customer_order_display']
            activation_description=item['activation_description']
            drivethru_date=item['drivethru_date']
            drive_store_site_name=item['store__site_name']
            total_score_drivethru += activation_on_promo_score

        deliveryqueryset = Delivery.objects.select_related('store').values('employee_no','mc_delivery','third_party_del','description_delivery','delivery_date','store__site_name')
        deliveryqueryset = deliveryqueryset.filter(store__site_name=selected_store,delivery_date__range=[from_date, to_date])
        for item in deliveryqueryset:
            mc_delivery_score = 1 if item['mc_delivery'] else 0
            third_party_del_score = 1 if item['third_party_del'] else 0

            mc_delivery=item['mc_delivery']
            third_party_del=item['third_party_del']
            description_delivery=item['description_delivery']
            delivery_date=item['delivery_date']
            store_site_name=item['store__site_name']
            total_score_delivery += mc_delivery_score+third_party_del_score
        


        data.append({'out_campaign_outside_store_site_name':out_campaign_outside_store_site_name,'out_campaign_outside_date':out_campaign_outside_date,'out_store_site_name':out_store_site_name,'out_description_inside_date':out_description_inside_date,'description_menu_store_site_name':description_menu_store_site_name,'description_menu_date':description_menu_date,'mccafe_store_site_name':mccafe_store_site_name,'mccafe_date':mccafe_date,'drive_store_site_name':drive_store_site_name,'drivethru_date':drivethru_date,'store_site_name':store_site_name,'delivery_date':delivery_date,'description_delivery':description_delivery,'target_delivery':target_delivery,'third_party_del':third_party_del,'mc_delivery':mc_delivery,'total_score_delivery':total_score_delivery,'activation_description':activation_description,'customer_order_display':customer_order_display,'drivethru_campaign':drivethru_campaign,'target_drivethru':target_drivethru,'activation_on_promo':activation_on_promo,'total_score_drivethru':total_score_drivethru,'description_mccafe':description_mccafe,'menu_promo':menu_promo,'mccafemenu_visibility':mccafemenu_visibility,'target_mccafe':target_mccafe,'total_score_Mccafe':total_score_Mccafe,'description_menu':description_menu,'menu_promotion':menu_promotion,'price_visibility':price_visibility,'out_description_inside':out_description_inside,'out_happy_m_campaign':out_happy_m_campaign,'out_promo_sok_campaigns':out_promo_sok_campaigns,'out_description_outside':out_description_outside,'out_campaigns':out_campaigns,'total_score_Main': total_score_Main,'menu_visibility':menu_visibility,'target_menu':target_menu,'total_score_inside': total_score_inside,'out_point_of_sale':out_point_of_sale,'out_self_order_kiosk':out_self_order_kiosk,'target_inside':target_inside,'total_score_outside': total_score_outside,'out_campaign':out_campaign, 'target_outside': target_outside, 'selected_store': selected_store,'out_branding_condition':out_branding_condition,'out_signage_condition':out_signage_condition})
    return JsonResponse(data, safe=False)
