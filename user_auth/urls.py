from django.urls import path
from .views import LoginPageView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/',LoginPageView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(),name='logout')
]