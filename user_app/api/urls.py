from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import registraction_view, logout_view

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', registraction_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
