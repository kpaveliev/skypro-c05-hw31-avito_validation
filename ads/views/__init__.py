from .ad import AdListView, AdDetailView, AdUpdateView, AdImageView, AdDeleteView, AdCreateView
# from .category import CategoryListView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView, CategoryCreateView, \
from .category import CategoryViewSet
from .location import LocationViewSet
from .selection import (SelectionListView, SelectionDetailView, SelectionCreateView,
                        SelectionUpdateView, SelectionDeleteView)
from .index import index

__all__ = [
    'AdListView',
    'AdDetailView',
    'AdUpdateView',
    'AdImageView',
    'AdDeleteView',
    'AdCreateView',
    # 'CategoryListView',
    # 'CategoryDetailView',
    # 'CategoryUpdateView',
    # 'CategoryDeleteView',
    # 'CategoryCreateView',
    'CategoryViewSet',
    'LocationViewSet',
    'SelectionListView',
    'SelectionDetailView',
    'SelectionCreateView',
    'SelectionUpdateView',
    'SelectionDeleteView',
    'index',
]
