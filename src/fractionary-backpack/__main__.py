
def fractional_knapsack(items: list[tuple[int, int]], W: int) -> float:
    # Sorteio uma nova lista que contém o peso, o valor e a eficiência
    efficiency = sorted([(item[0], item[1], item[1]/item[0]) for item in items], key=lambda item: item[2], reverse=True)

    backpack = []
    w = 0

    for item in efficiency:
        if w + item[0] > W:
            alpha = (w + item[0] - W) / item[0]
            new_weight = item[0] * (1 - alpha)
            new_value = item[1] * (1 - alpha)
            new_efficiency = item[1]/item[0]

            backpack.append((new_weight, new_value, new_efficiency))
            w += new_weight
            break
        else:
            backpack.append(item)
            w += item[0]
    
    return backpack
