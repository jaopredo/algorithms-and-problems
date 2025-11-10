
def compare_lists(A, B):
        invs = 0
        n = len(A)
        for j in range(len(B)):
            i = 0
            while A[i] <= B[j]:
                i += 1
                if i >= n:
                    break
            invs += n - i
        return invs


def inversions_counter(A):
    n = len(A)
    if n==1:
        return 0
    else:
        L = A[:n//2]
        R = A[n//2:]
        
        i_l = inversions_counter(L)
        i_r = inversions_counter(R)

        L = sorted(L)
        R = sorted(R)

        i = compare_lists(L, R)

        return i + i_l + i_r


print(inversions_counter([2,5,4,1,9,7,6,11,3,12,8,10]))
print(inversions_counter([3,7,2,9,5]))
print(inversions_counter([1,2,3]))
print(inversions_counter([3,2,1]))
