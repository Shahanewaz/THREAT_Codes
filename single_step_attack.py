from llm_generation import LLM_generate_variant
from utils import compute_similarity, f_safe, f_safe_gpt

def SafePromptAttack(x, f_safe, S, epsilon1, epsilon2, N):
    """
    Finds the most safe semantically similar variant of the prompt x.
    """
    base_score = f_safe(x)
    # print(base_score)
    
    R_best = float('-inf')
    x_best = None

    for i in range(N):
        x_variant = LLM_generate_variant(x)
        
        x_variant = None if x_variant and (
            any(p in x_variant.lower() for p in [
                "i'm sorry", "i can’t assist", "i can't assist", "i cannot assist", "i'm unable", 
                "iâ€™m sorry", "i canâ€™t assist", "as a language model, iâ€™m unable to assist with that request",
                "i am unable to assist with that request", "i am currently unable to assist with that request"
            ]) or x_variant.lower().startswith("as an ai language model")
        ) else x_variant
        
        if x_variant is None:
            continue

        similarity = S(x, x_variant)
        
        if epsilon1 <= similarity <= epsilon2:
            score_variant = f_safe(x_variant)
            R = score_variant - base_score

            if R > R_best:
                R_best = R
                x_best = x_variant
    
    if x_best is None:
        return None, 0

    return x_best, R_best
