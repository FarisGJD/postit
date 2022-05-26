from .import views 
from django.urls import path 


urlpatterns = [
    # path('', views.ThreadList.as_view(), name="home"),
    path('', views.postit_list, name="home"),
    path('postit/', views.postit_tempalte, name="postit"),
    path('profile/', views.profile_tempalte, name="profile")
]
