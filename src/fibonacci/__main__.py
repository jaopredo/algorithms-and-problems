
def fibonacci_1(n):
    if n <= 3:
        return 1
    else:
        return fibonacci_1(n-1) + fibonacci_1(n-2)


def fibonacci_2(n):
    cache = [0, 1, 1]
    if n > 3:
        cache += [-1 for _ in range(n-3)]

    def find_value(n):
        if cache[n-1] != -1:
            return cache[n-1]
        else:
            first = cache[n-2] if cache[n-2] != -1 else find_value(n-1)
            second = cache[n-3] if cache[n-3] != -1 else find_value(n-2)
            cache[n-1] = first+second
            return cache[n-1]

    return find_value(n)


def fibonacci_3(n):
    phi = (1+5**(1/2))/2

    return int(1/(5**(1/2)) * (phi**(n-1) - (-1/phi)**(n-1)))
