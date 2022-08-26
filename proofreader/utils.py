from gramformer import Gramformer
import torch


def set_seed(seed):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


set_seed(1212)

gf = Gramformer(models=1, use_gpu=False)  # 1=corrector, 2=detector


def text_proofreading(influent_sentences=["fixed your", "Spelling"]):
    for influent_sentence in influent_sentences:
        context = {}
        corrected_sentences = gf.correct(influent_sentence, max_candidates=1)
        print("[Input] ", influent_sentence)
        context['input'] = influent_sentence
        for corrected_sentence in corrected_sentences:
            print("[Correction] ", corrected_sentence)
            context['correction'] = influent_sentence

        print("-" * 100)
        return context
