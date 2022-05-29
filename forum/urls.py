from .import views 
from django.urls import path 


urlpatterns = [
    path('', views.postit_list, name="home"),
    path('<slug:slug>/', views.FullThread.as_view(), name="full_thread"),
    path('add', views.create_postit, name="add"),
    path('edit/<postit_id>', views.edit_postit, name='edit'),
    path('delete/<postit_id>', views.delete_postit, name='delete'),
    path('profile/', views.profile_list, name="profile"),
]
