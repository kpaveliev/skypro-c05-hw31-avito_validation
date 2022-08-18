from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):

    def get(self, request):
        """Display all categories"""
        categories = Category.objects.all()

        response = [
            {
                'id': category.id,
                'name': category.name
            }
            for category in categories
        ]

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        """Add category to database"""
        category_data = json.loads(request.body)
        category = Category.objects.create(**category_data)

        response = {
                'id': category.id,
                'name': category.name
        }

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})


class CategoryDetailView(DetailView):
    model = Category

    def get(self, *args, **kwargs):
        category = self.get_object()

        response = {
                'id': category.id,
                'name': category.name
        }

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})
