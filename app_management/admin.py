from django.contrib import admin

# Register your models here.
from .models import Province, Store,Store_Map,StorePerformance,EntranceEvaluation,Store_level,Employee,Inside,Outside,Menu,McCafe,Drivethru,Delivery

admin.site.register(Province)
admin.site.register(Store_Map)
admin.site.register(Store_level)
admin.site.register(Employee)
admin.site.register(Inside)
admin.site.register(Outside)
admin.site.register(Menu)
admin.site.register(McCafe)
admin.site.register(Drivethru)
admin.site.register(Delivery)
