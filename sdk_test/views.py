from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from sdk_test import utils
import base64


class ImageView(TemplateView):
    """
    Return Image
    """
    template_name = 'image.html'

    def get(self, request, *args, **kwargs):
        word = request.GET.get('text', 'Demo Image')
        print(word)
        # api_key = request.get["key"]
        my_image = utils.get_image(word, api_key=settings.STABILITY_KEY)
        # qr.save(my_image, kind='PNG')
        context = {
            'image': base64.b64encode(my_image.getvalue()).decode('utf-8'),
        }
        print(my_image)
        return render(request, 'image.html', context=context)

    def post(self, request, *args, **kwargs):
        word = request.POST.get('text', '')
        print(word)
        # api_key = request.get["key"]
        my_image = utils.get_image(word, api_key=settings.STABILITY_KEY)
        context = {
            'image': base64.b64encode(my_image.getvalue()).decode('utf-8'),
        }
        print(my_image)
        return render(request, 'image.html', context=context)
