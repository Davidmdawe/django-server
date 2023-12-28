from django.contrib import admin

# Register your models here.
from .models import Province, Store,Store_Map,StorePerformance,EntranceEvaluation,Store_level,Employee,Inside,Outside,Menu,McCafe,Drivethru,Delivery

admin.site.register(Menu)