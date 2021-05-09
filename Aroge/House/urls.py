from django.urls import path, include
from . import views

urlpatterns = [    
    path('list/', views.house_list, name='house_list'),
    path('detail/<int:house_id>/', views.house_detail, name='house_detail'),

]