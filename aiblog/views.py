from django.shortcuts import render
from django.views.generic import TemplateView
from .utils import generate_blog_topics, generate_blog_sections, blog_section_expander


class GenerateBlogTopicsView(TemplateView):
    """
    View to Generate Blog topics
    """
    template_name = 'ai_blog.html'

    def post(self, request, *args, **kwargs):
        my_test = request.POST.get('ai-blog-input', '')
        context = generate_blog_topics(my_test)

        return render(request, 'ai_blog.html', context=context)


class GenerateBlogSectionsView(TemplateView):
    """
       View to Generate Blog topics
    """
    template_name = 'ai_blog.html'

    def post(self, request, *args, **kwargs):
        my_test = request.POST.get('ai-blog-input', '')
        my_test1 = request.POST.get('ai-blog-input-parent', '')
        context = generate_blog_sections(my_test, my_test1)

        return render(request, 'ai_blog.html', context=context)


class BlogSectionExpanderView(TemplateView):
    """
       View to Generate Blog topics
    """
    template_name = 'ai_blog.html'

    def post(self, request, *args, **kwargs):
        my_test = request.POST.get('ai-blog-input', '')
        my_test1 = request.POST.get('ai-blog-input-parent', '')
        context = blog_section_expander(my_test, my_test1)

        return render(request, 'ai_blog.html', context=context)
