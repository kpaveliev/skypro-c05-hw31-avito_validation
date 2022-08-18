from django.urls import path

from ads.views import (AdView, AdDetailView,
                       CategoryListView, CategoryDetailView, CategoryCreateView,
                       index)

urlpatterns = [
    path('', index),
    path('ad/', AdView.as_view()),
    path('ad/<int:pk>/', AdDetailView.as_view()),
    path('cat/', CategoryListView.as_view()),
    path('cat/<int:pk>/', CategoryDetailView.as_view()),
    path('cat/create/', CategoryCreateView.as_view()),
]
