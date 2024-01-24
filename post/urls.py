from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('',views.post_list ,name='post_list'),
    path('<int:id>',views.post_detail,name='post_detail'),
    path('<int:id>/edit',views.post_edit,name='post_edit'),
    path('create',views.post_create,name='post_create'),
    
    
    path('cbv',views.PostList.as_view(), name='post_list_cbv'),
    path('cbv/create',views.PostCreate.as_view(), name='post_create_cbv'),
    
    path('cbv/<int:pk>',views.PostCreate.as_view(),name='post_detail_cbv'),
    path('cbv/<int:pk>/edit',views.PostUpdate.as_view(),name='post_update_cbv'),
   
    


]