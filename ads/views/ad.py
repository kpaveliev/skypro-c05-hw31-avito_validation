from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ad


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):

    def get(self, request):
        """Display all ads"""
        ads = Ad.objects.all()

        response = [
            {
                'id': ad.id,
                'author': ad.author,
                'name': ad.name,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
                'is_published': ad.is_published
            }
            for ad in ads
        ]

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        """Add ad to database"""
        ad_data = json.loads(request.body)
        ad = Ad.objects.create(**ad_data)

        response = {
                'id': ad.id,
                'author': ad.author,
                'name': ad.name,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
                'is_published': ad.is_published
        }

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})


class AdDetailView(DetailView):
    model = Ad

    def get(self, *args, **kwargs):
        ad = self.get_object()

        response = {
                'id': ad.id,
                'author': ad.author,
                'name': ad.name,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
                'is_published': ad.is_published
        }

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})
