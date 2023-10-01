from django.urls import path

from .views import index, logout_view, login_view

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('loginout/', logout_view, name='logout_view'),
]
