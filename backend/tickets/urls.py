from django.urls import path
from .views import ticket_list,ticket_detail,register_user
urlpatterns = [
    
    path('tickets/',ticket_list,name='ticket_list'),
    path('tickets/<int:id>/',ticket_detail,name='ticket_detail'),
    path('register/',register_user,name='registration')

]