from django.urls import path

from ads.views import (AdView, AdDetailView,
                       CategoryView, CategoryDetailView,
                       index)

urlpatterns = [
    path('', index),
    path('ad/', AdView.as_view()),
    path('ad/<int:pk>/', AdDetailView.as_view()),
    path('cat/', CategoryView.as_view()),
    path('cat/<int:pk>/', CategoryDetailView.as_view()),
]
