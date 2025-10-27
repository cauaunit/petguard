from django.urls import path
from petguard import views

urlpatterns = [
    path('', views.login_view, name='login'),   # página de login
    path('index/', views.index, name='index'),  # página principal
    path('logout/', views.logout_view, name='logout'),  # logout
]
