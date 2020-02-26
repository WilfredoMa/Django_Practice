from .views import BlogPostRUDView, BlogPostDetailView
from django.urls import path

urlpatterns = [
    path('', BlogPostRUDView.as_view()),
    path('<pk>/', BlogPostDetailView.as_view()),
]