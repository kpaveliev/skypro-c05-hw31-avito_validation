from django.urls import path

from ads.views import (AdListView, AdDetailView, AdCreateView,
                       CategoryListView, CategoryDetailView, CategoryCreateView,
                       index)

urlpatterns = [
    path('', index),
    path('ad/', AdListView.as_view()),
    path('ad/<int:pk>/', AdDetailView.as_view()),
    path('ad/create/', AdCreateView.as_view()),
    path('cat/', CategoryListView.as_view()),
    path('cat/<int:pk>/', CategoryDetailView.as_view()),
    path('cat/create/', CategoryCreateView.as_view()),
]
