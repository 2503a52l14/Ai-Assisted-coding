import time

def optimized_file_processing(file_path):
    """Optimized method: Uses generator expressions for efficiency."""
    with open(file_path, 'r') as file:
        result = (line.strip() for line in file if 'ERROR' in line)
        return list(result)

def compare_performance(file_path):
    """Compares the performance of the optimized method."""
    print("Comparing performance...")

    start_time = time.time()
    optimized_result = optimized_file_processing(file_path)
    optimized_time = time.time() - start_time

    print(f"Optimized method time: {optimized_time:.6f} seconds")

if __name__ == "__main__":
    # Replace 'large_log_file.txt' with the path to your log file
    log_file_path = "large_log_file.txt"
    compare_performance(log_file_path)