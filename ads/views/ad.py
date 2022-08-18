import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView

from ads.models import Ad


class AdListView(ListView):
    """Display all ads"""
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        ads = self.object_list

        response = [
            {
                'id': ad.id,
                'author': str(ad.author),
                'name': ad.name,
                'price': ad.price,
                'description': ad.description,
                'is_published': ad.is_published,
                'category': str(ad.category)
            }
            for ad in ads
        ]

        return JsonResponse(response,
                            safe=False,
                            json_dumps_params={"ensure_ascii": False})


class AdDetailView(DetailView):
    model = Ad

    def get(self, *args, **kwargs):
        ad = self.get_object()

        response = {
                'id': ad.id,
                'author': str(ad.author),
                'name': ad.name,
                'price': ad.price,
                'description': ad.description,
                'is_published': ad.is_published,
                'category': str(ad.category)
        }

        return JsonResponse(response,
                            json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ['name', 'author', 'price', 'description', 'is_published', 'image', 'category']

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)
        ad = Ad.objects.create(**ad_data)

        response = {
                'id': ad.id,
                'author': str(ad.author),
                'name': ad.name,
                'price': ad.price,
                'description': ad.description,
                'is_published': ad.is_published,
                'category': str(ad.category)
        }

        return JsonResponse(response,
                            json_dumps_params={"ensure_ascii": False})
