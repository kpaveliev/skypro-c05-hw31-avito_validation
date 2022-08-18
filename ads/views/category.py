import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView

from ads.models import Category


class CategoryListView(ListView):
    """Show all categories"""
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        categories = self.object_list

        response = [
            {
                'id': category.id,
                'name': category.name
            }
            for category in categories
        ]

        return JsonResponse(response,
                            safe=False,
                            json_dumps_params={"ensure_ascii": False})


class CategoryDetailView(DetailView):
    """Show category by id"""
    model = Category

    def get(self, *args, **kwargs):
        category = self.get_object()

        response = {
                'id': category.id,
                'name': category.name
        }

        return JsonResponse(response,
                            json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    """Create category"""
    model = Category
    fields = ['name']

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)
        category = Category.objects.create(**category_data)

        response = {
                'id': category.id,
                'name': category.name
        }

        return JsonResponse(response,
                            json_dumps_params={"ensure_ascii": False})


