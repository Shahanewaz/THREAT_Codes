from attack_framework import IterativeSafePromptAttack
from utils import f_safe_gpt, compute_similarity
from single_step_attack import SafePromptAttack  

def optimize_prompt(x_init):
    x_best, R_best = IterativeSafePromptAttack(
        x_init = x_init,
        f_safe = f_safe_gpt,
        S = compute_similarity,
        epsilon1 = 0.05,
        epsilon2 = 0.98,
        N = 5,
        max_iters = 5
    )
    return x_best, R_best