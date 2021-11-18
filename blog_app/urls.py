from django.urls import path

from .views import (BlogPostListView,
                    BlogPostDetailView,
                    BlogPostFeaturedView, 
                    BlogPostCategoryView,
                    FeedbackView,)


urlpatterns = [
    path('', BlogPostListView.as_view(), name = 'blog_list'),
    path('<slug>/', BlogPostDetailView.as_view(), name = 'blog_detail'),
    path('featured', BlogPostFeaturedView.as_view(), name = 'featured'),
    path('category', BlogPostCategoryView.as_view(), name = 'category'),
    path('feedback', FeedbackView.as_view(), name = 'feedback'),
    ]