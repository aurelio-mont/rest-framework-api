from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]