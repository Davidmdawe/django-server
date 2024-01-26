
from django.urls import path
from .views import login_view, home_view,logout_view,get_store_data,MapDataView,get_store_data_store_level,visuals_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('visuals/', visuals_view, name='visuals'),
    path('logout/', logout_view, name='logout'),
    path('get_store_data_store_level/', get_store_data_store_level, name='get_store_data_store_level'),
    path('get_store_data/', get_store_data, name='get_store_data'),
    path('get_map_data/', MapDataView.as_view(), name='get_map_data'),
    # Add other URL patterns as needed
]