def rolling_mean(xs, w):
    """
    Calculate the rolling mean of a list of numbers with a given window size.

    Args:
        xs (list): List of numbers.
        w (int): Window size.

    Returns:
        list: List of rolling means.
    """
    if w <= 0 or w > len(xs):
        raise ValueError("Window size must be greater than 0 and less than or equal to the length of the list.")

    means = []
    for i in range(len(xs) - w + 1):  # Fix: Include all valid windows
        window = xs[i:i + w]
        means.append(sum(window) / w)
    return means

# Quick test
if __name__ == "__main__":
    xs = [15, 16, 17, 18]
    w = 2

    result = rolling_mean(xs, w)
    print(result)  # Expected output: [15.5, 16.5, 17.5]