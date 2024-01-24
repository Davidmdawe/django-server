from django.contrib import admin
# Register your models here.
from .models import Shops as Store_level,Inside,Outside,Menu,Mccafe as McCafe,Drivethru as Drivethru,Delivery as Delivery

admin.site.register(Store_level)
admin.site.register(Inside)
admin.site.register(Outside)
admin.site.register(Menu)
admin.site.register(McCafe)
admin.site.register(Drivethru)
admin.site.register(Delivery)
