
def min_and_max_val(A: list[float|int]):
    if not A:
        return float('inf'), -float('inf')
    
    def min_and_max_AUX(i, j):
        if j - i + 1 <= 3:
            return min(A[i:j+1]), max(A[i:j+1])
        else:
            k = (i + j)//2
            minimum1, maximum1 = min_and_max_AUX(i, k)
            minimum2, maximum2 = min_and_max_AUX(k+1, j)
            return min(minimum1, minimum2), max(maximum1, maximum2)
    
    return min_and_max_AUX(0, len(A)-1)
