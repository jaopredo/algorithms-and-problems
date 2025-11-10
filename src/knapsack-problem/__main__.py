import numpy as np


def knupsack_problem_top_down(n: int, v: list[int|float], w: list[int|float], W: int):
    M = np.full((n+1, W+1), -1)

    def knupsack_aux(i, W):
        if i == 0 or W == 0:
            return 0
        if M[i, W] == -1:
            if w[i-1] > W:
                M[i,W] = knupsack_aux(i-1, W)
            else:
                using = v[i-1] + knupsack_aux(i-1, W - w[i-1])
                not_using = knupsack_aux(i-1, W)
                M[i, W] = max(using, not_using)
        return M[i,W]
    
    return knupsack_aux(n, W)


def knupsack_problem_bottom_up(n: int, v: list[int|float], w: list[int|float], W: int):
    M = np.zeros((n+1, W+1))

    def knupsack_aux(i, j):
        if w[j-1] > i:
            M[j, i] = M[j-1,i]
        else:
            using = v[j-1] + M[j-1, i-w[j-1]]
            not_using = M[j-1, i]
            M[j, i] = max(using, not_using)

    for j in range(1,n+1):
        for i in range(1, W+1):
            knupsack_aux(i, j)
    
    return M[n, W]
