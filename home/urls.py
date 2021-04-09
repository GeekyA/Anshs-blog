from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.posts,name='index'),
    path('<int:post_id>',views.content,name='content'),
    path('search',views.search_results,name='search_results')
]
