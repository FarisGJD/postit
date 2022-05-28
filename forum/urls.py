from .import views 
from django.urls import path 


urlpatterns = [
    path('', views.postit_list, name="home"),
    path('postit/', views.create_postit, name="postit"),
    path('profile/', views.profile_list, name="profile"),
]
