# The safety score variable $\lambda$ was hard coded to be 0.95

from single_step_attack import SafePromptAttack

def IterativeSafePromptAttack(x_init, f_safe, S, epsilon1, epsilon2, N, max_iters):
    x_current = x_init
    base_score = f_safe(x_init)
    best_R = 0
    x_final = x_init

    for t in range(max_iters):
        x_next, R = SafePromptAttack(x_current, f_safe, S, epsilon1, epsilon2, N)
        # print(x_next)

        if x_next is None or R <= 0:
            # print(f"[Iteration {t}] No further improvement. Stopping.")
            break

        x_current = x_next
        total_gain = f_safe(x_current) - base_score

        if total_gain > best_R:
            best_R = total_gain
            x_final = x_current

        # print(f"[Iteration {t}] Best R so far: {best_R:.3f}")

    return x_final, best_R
