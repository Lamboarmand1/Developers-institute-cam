from django.urls import path
from . import views

urlpatterns=[
	path('info/', views.info, name='info'),
	path('login/', views.login_, name='login'),
	path('logout/', views.logout_, name='logout'),
	path('reservation/<date_in>/<date_out>/<room_id>', views.reservation, name='reservation')
]
