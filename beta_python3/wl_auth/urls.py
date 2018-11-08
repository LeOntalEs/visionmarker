from django.urls import path
from . import views
app_name = 'wl_auth'
urlpatterns = [
	path('signin/', views.signin, name='signin'),
	path('signout/', views.signout, name='signout'),
	path('change_password/', views.change_password, name='change_password'),
	path('singup/',views.signup,name='singup'),
]