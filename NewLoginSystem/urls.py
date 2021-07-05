from django.conf.urls import url, include
from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    # Main View
    url(r'^$', views.home, name='home'),
    url('login/', views.login, name='login'),
    url('signup/', views.signup, name='signup'),
    url('logout/', views.logout, name='logout'),
    # url('update/', views.update, name='update'),

    # offer master urls
    path('offer-master/create', views.offer_master_new, name="offer_master_new"),
    path('offer-master/view', views.view_query_offer, name="view_query_offer"),
    path('offer-master/result/', views.view_query_show_offer),
    path('offer-master/update/<int:pk>/', views.update_offer, name="update_offer"),
    path('offer-master/delete/<int:pk>/', views.delete_offer, name='delete_offer'),

]
