from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from django.urls import path

urlpatterns = [
    path('',PostListView.as_view(), name = 'flick-home'),
    path('user/<username>',UserPostListView.as_view(), name = 'flick-user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(), name = 'flick-post'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name = 'flick-post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name = 'flick-post-delete'),
    path('post/new/',PostCreateView.as_view(), name = 'flick-post-create'),
    path('about/',views.about, name = 'flick-about'),
    path('facebook/',views.facebook, name = 'facebook'),
    path('contact/',views.contact, name = 'flick-contact'),
]