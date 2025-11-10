
def closest_pair(points: list[tuple[float, float]]):
    points.sort(key=lambda p: (p[0], p[1]))

    def find_distance(points):
        n = len(points)
        if n <= 3:
            min_dist = float('inf')
            pair = None

            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                    d2 = sum((points[i][k] - points[j][k])**2 for k in range(len(points[i])))
                    if d2 < min_dist:
                        min_dist = d2
                        pair = [i, j]

            return (min_dist**0.5, pair)
        else:
            # Divide it in two groups
            A = points[:n//2]
            B = points[n//2:]

            # Get the best distance inside each group and the points
            d1, pAs = find_distance(A)
            d2, pBs = find_distance(B)

            threshold = (A[-1][0] + B[0][0])/2
            best_d = min(d1, d2)

            C = []
            # I'm going to go just after the point I compared in the
            # first group and on
            for i in range(pAs[1], n//2-1):
                if abs(A[i][0] - threshold) <= best_d:
                    C.append(A[i])
            
            for j in range(n//2, pBs[0]+1):
                if abs(B[j][0] - threshold) <= best_d:
                    C.append(B[j])
            
            C.sort(key=lambda p: p[1])
            
            # Now I apply the algorithm on C
            d3, pCs = find_distance(C)

            return min([
                (d1, pAs), (d2, pBs), (d3, pCs)
            ], key=lambda info: info[0])

    
    return find_distance(points)[0]

print(closest_pair([(0,0),(1,1),(0,2),(2,0)]))
print(closest_pair([(10,5),(12,5),(10,15)]))
