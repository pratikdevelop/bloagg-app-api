
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.getToken),
    path('logout', views.logout),
    path('signup', views.signup),
    path('signin', views.signin),
]
