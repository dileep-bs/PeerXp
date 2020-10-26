from . import views
from django.urls import path
# from views import TicketView

urlpatterns=[
    path('',views.index,name='index'),
    path('logout/',views.logout_request,name='logout'),
    # path('raise_ticket/',views.TicketView.as_view(),name='raise_ticket'),
    path('raise_ticket/',views.raise_ticket,name='raise_ticket'),
    path('view_tickets/',views.Alltickets.as_view(),name='view_tickets'),
    path('login/',views.login,name='login'),
]