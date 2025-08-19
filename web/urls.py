from django.urls import path
from . import views 
from .views import change_password
from django.views.generic import TemplateView

urlpatterns = [    
path('login/', views.loginPage, name= 'login'),
path('user_list/', views.user_list, name= 'user_list'),
path('cashflow/', views.cashflow, name='cashflow'),
path('insert/', views.insert, name= 'insert'),
path('logout/', views.logoutUser, name= 'logout'),
path('register/', views.registerPage, name= 'register'),
path('', views.home, name='home'),
path('index/<str:pk>/', views.index, name='index'),
path('createRoom/', views.createRoom, name='createRoom'),
path('updateRoom/<str:pk>/', views.updateRoom, name='updateRoom'),
path('deleteRoom/<str:pk>/', views.deleteRoom, name='deleteRoom'),
path('cashflow/', views.cashflow, name='cashflow'),  
path('pdf/', views.pdf, name='pdf'),
path('detail/<str:pk>/', views.people, name='detail'),
path('Panel/', views.Panel, name='Panel'),
path('single/', views.single, name='single'),
path('members/', views.members, name='members'),
path('Message/', views.Message, name='Message'),
path('Msge/', views.Msge, name='Msge'),
path('gci/', views.gci_groups, name='gci'),
path('meso/', views.meso, name='meso'),
path('password/change/', change_password, name='password_change'),
path('password/change/done/', TemplateView.as_view(template_name='web/password_change_done.html'), name='password_change_done'),
#path('accounts/', include('django.contrib.auth.urls')),
path('deleteRecord/<str:pk>/', views.deleteRecord, name='deleteRecord'),

]