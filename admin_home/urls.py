from django.urls import path
from .import views



urlpatterns = [
    # .............................................................................................................
    
    path('',views.admin_home,name="admin_home"),
    path('login/',views.admin_login,name="admin_login"),
    path('logout/',views.admin_logout,name="admin_logout"),


    

  


]