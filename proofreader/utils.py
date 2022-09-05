from django.conf import settings

from gramformer import Gramformer
import torch
import openai


def set_seed(seed):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


set_seed(1212)

gf = Gramformer(models=1, use_gpu=False)  # 1=corrector, 2=detector


def text_proofreading(influent_sentences=["fixed your", "Spelling"]):
    context = {}
    my_text = ""
    correct_text = ""
    for influent_sentence in influent_sentences:
        corrected_sentences = gf.correct(influent_sentence, max_candidates=1)
        my_text += influent_sentence
        for corrected_sentence in corrected_sentences:
            correct_text += corrected_sentence
        context['input'] = my_text
        context['correction'] = correct_text
    return context


def ai_proofreading(prompt):
    openai.api_key = settings.OPEN_AI_KEY
    context = {}
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Correct this to standard English:\n\n" + prompt,
        temperature=0,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    context['input'] = prompt
    context['correction'] = response['choices'][0]['text']
    return context
