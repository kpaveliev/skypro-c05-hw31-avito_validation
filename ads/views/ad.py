import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

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
                'author_id': ad.author_id,
                'author': str(ad.author),
                'name': ad.name,
                'price': ad.price,
                'description': ad.description,
                'is_published': ad.is_published,
                'image': ad.image.url if ad.image else None,
                'category_id': ad.category_id,
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
            'author_id': ad.author_id,
            'author': str(ad.author),
            'name': ad.name,
            'price': ad.price,
            'description': ad.description,
            'is_published': ad.is_published,
            'image': ad.image.url if ad.image else None,
            'category_id': ad.category_id,
            'category': str(ad.category)
        }

        return JsonResponse(response,
                            json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = ['name', 'price', 'description', 'is_published', 'image', 'category']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ad_data = json.loads(request.body)
        ad = self.object

        ad.name = ad_data.get('name')
        ad.price = ad_data.get('price')
        ad.description = ad_data.get('description')
        ad.is_published = ad_data.get('is_published')
        ad.category_id = ad_data.get('category_id')

        ad.save()

        response = {
            'id': ad.id,
            'author_id': ad.author_id,
            'author': str(ad.author),
            'name': ad.name,
            'price': ad.price,
            'description': ad.description,
            'is_published': ad.is_published,
            'image': ad.image.url if ad.image else None,
            'category_id': ad.category_id,
            'category': str(ad.category)
        }

        return JsonResponse(response,
                            json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = Ad
    fields = ['name', 'image']

    def post(self, request, *args, **kwargs):

        ad = self.get_object()
        ad.image = request.FILES['image']
        ad.save()

        response = {
            'id': ad.id,
            'author_id': ad.author_id,
            'author': str(ad.author),
            'name': ad.name,
            'price': ad.price,
            'description': ad.description,
            'is_published': ad.is_published,
            'image': ad.image.url if ad.image else None,
            'category_id': ad.category_id,
            'category': str(ad.category)
        }

        return JsonResponse(response,
                            json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'OK'},
                            status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ['name', 'author', 'price', 'description', 'is_published', 'image', 'category']

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)
        ad = Ad.objects.create(**ad_data)

        response = {
            'id': ad.id,
            'author_id': ad.author_id,
            'author': str(ad.author),
            'name': ad.name,
            'price': ad.price,
            'description': ad.description,
            'is_published': ad.is_published,
            'image': ad.image.url if ad.image else None,
            'category_id': ad.category_id,
            'category': str(ad.category)
        }

        return JsonResponse(response,
                            json_dumps_params={"ensure_ascii": False})
