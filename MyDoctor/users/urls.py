from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inup/', views.signin_signup_view, name = 'inup'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Logs out and redirects to homepage

]
