from django.http import HttpResponse  # last line below allows MyView.get
# to return an HttpResponse object
from django.views.generic import TemplateView
from django.conf import settings
from sdk_test import utils


class ImageView(TemplateView):
    """
    Return Image
    """
    template_name = 'image.html'

    def get(self, request, *args, **kwargs):
        word = request.GET.get('text', '')
        print(word)
        # api_key = request.get["key"]
        my_image = utils.get_image(word, api_key=settings.STABILITY_KEY)
        print(my_image)
        return HttpResponse(my_image)

    def post(self, request, *args, **kwargs):
        pass
