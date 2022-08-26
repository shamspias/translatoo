from gramformer import Gramformer
import torch


def set_seed(seed):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


set_seed(1212)

gf = Gramformer(models=1, use_gpu=False)  # 1=corrector, 2=detector

influent_sentences = [
    " My name is luka and I love to eat saur fruts "
]

for influent_sentence in influent_sentences:
    corrected_sentences = gf.correct(influent_sentence, max_candidates=1)
    print("[Input] ", influent_sentence)
    for corrected_sentence in corrected_sentences:
        print("[Correction] ", corrected_sentence)
    print("-" * 100)
