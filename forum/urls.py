from .import views 
from django.urls import path 


urlpatterns = [
    path('', views.home_template, name="home"),
    path('postit/', views.get_postit_items, name="postit"),
    path('profile/', views.profile_tempalte, name="profile")
]
