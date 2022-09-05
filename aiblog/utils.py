from django.conf import settings
import openai

openai.api_key = settings.OPEN_AI_KEY


def generate_blog_topics(prompt):
    context = {}
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate blog topics on: {}. \n \n 1.  ".format(prompt),
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    context['input'] = prompt
    context['correction'] = response['choices'][0]['text']
    return context


def generate_blog_sections(prompt):
    context = {}
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Expand the blog title in to high level blog sections: {} \n\n- Introduction: ".format(prompt),
        temperature=0.6,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    context['input'] = prompt
    context['correction'] = response['choices'][0]['text']
    return context


def blog_section_expander(prompt):
    context = {}
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Expand the blog section in to a detailed professional , witty and clever explanation.\n\n {}".format(
            prompt),
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    context['input'] = prompt
    context['correction'] = response['choices'][0]['text']
    return context
