def optimization(A: list[int]) -> int:
    """
    Dado um vetor $A$ com $n$ inteiros, projete um algoritmo linear que retorna
    o menor valor inteiro $k$ que minimiza a soma:
    $$ \\sum_{i=1}^{n} |A_i-k| $$
    A complexidade de tempo deve ser $O(n)$.
    """
    def swap(v,i,j):
        temp = v[i]
        v[i]=v[j]
        v[j]=temp
    
    def partition(v, p, r, pivot=None):
        # se não foi passado um pivô, usa o último elemento
        if pivot is None:
            pivot = v[r]
        
        # acha a posição real do pivot dentro de v[p:r+1]
        for i in range(p, r+1):
            if v[i] == pivot:
                swap(v, i, r)
                break
        
        j = p
        for i in range(p, r):
            if v[i] <= pivot:
                swap(v, i, j)
                j += 1
        swap(v, j, r)
        return j
    
    def medianOf(v, n):
        g = sorted(v)
        return g[n//2]
    
    def selectMOM(arr, left, right, k):
        n = right - left + 1

        if k <= 0 or k > n:
            return -1
        
        numGroups = (n+4)//5
        medians = []

        groupIndex = 0
        pos = left

        while pos <= right:
            groupSize = None

            if pos+4 <= right:
                groupSize = 5
            else:
                groupSize = right - pos + 1
            
            group = []
            for i in range(groupSize):
                group.append(arr[pos+i])
            
            med = medianOf(group, groupSize)
            medians.append(med)
            groupIndex+=1
            pos += 5
        
        pivotValue = None
        if numGroups == 1:
            pivotValue = medians[0]
        else:
            middleGroup = (numGroups+1) // 2
            pivotValue = selectMOM(medians, 0, numGroups - 1, middleGroup)

        pivotIndex = partition(arr, left, right, pivotValue)
        order = pivotIndex - left + 1

        if order == k:
            return arr[pivotIndex]
        elif order > k:
            return selectMOM(arr, left, pivotIndex - 1, k)
        else:
            return selectMOM(arr, pivotIndex+1, right, k - order)

    n = len(A)
    if n % 2 == 1:
        return selectMOM(A, 0, n-1, (n+1)//2)
    else:
        left = selectMOM(A, 0, n-1, n//2)
        right = selectMOM(A, 0, n-1, n//2 + 1)

        median = (left + right) / 2

        difs = [(abs(left - median), left), (abs(right - median), right)]
        result = min(difs, key=lambda d: d[0])[1]

        return result