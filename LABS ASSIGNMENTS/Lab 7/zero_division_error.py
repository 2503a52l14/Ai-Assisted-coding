def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i, len(values)):
            try:
                ratio = values[i] / (values[j] - values[i])
                results.append((i, j, ratio))
            except ZeroDivisionError:
                results.append((i, j, " Division by zero"))
    return results

nums = [5, 10, 15, 20, 25]
print(compute_ratios(nums))