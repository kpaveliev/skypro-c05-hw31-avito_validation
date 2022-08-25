import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView

from ads.models import Ad, Category
from ads.serializers.ad import AdSerializer
from users.models import User


class AdListView(ListAPIView):
    """Display all ads"""
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdDetailView(RetrieveAPIView):
    """Display ad by id"""
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ['name', 'author', 'price', 'description', 'is_published', 'image', 'category']

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)
        ad = Ad.objects.create(
            name=ad_data.get('name'),
            price=ad_data.get('price'),
            description=ad_data.get('description'),
            is_published=ad_data.get('is_published')
        )

        ad.author = get_object_or_404(User, pk=ad_data.get('author_id'))
        ad.category = get_object_or_404(Category, pk=ad_data.get('category_id'))
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


class AdDeleteView(DestroyAPIView):
    """Delete ad by id"""
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
