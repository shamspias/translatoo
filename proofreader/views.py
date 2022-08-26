from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from .utils import text_proofreading


class ProofreadingView(TemplateView):
    """
    View to Proofreading
    """
    template_name = 'proofreading.html'

    def post(self, request, *args, **kwargs):
        my_test = request.POST.get('proofreading', '')
        my_list_text = my_test.split('.', )
        context = text_proofreading(my_list_text)

        return render(request, 'proofreading.html', context=context)
