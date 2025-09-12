def process_sensor_data(data):
    """
    Process sensor data to clean it, calculate the average, and identify anomalies.

    Args:
        data (list): A list of sensor readings, which may include `None` values.

    Returns:
        dict: A dictionary containing:
            - "average" (float): The average of the cleaned data.
            - "anomalies" (list): A list of values that deviate from the average by more than 10 units.
            - "total_data_points" (int): The total number of data points in the input.
            - "cleaned_data_points" (int): The number of data points after cleaning.
            - "anomalies_count" (int): The number of anomalies detected.
    """
    # Step 1: Remove any `None` values from the input data to clean it.
    cleaned = [x for x in data if x is not None]
    
    # Step 2: Calculate the average of the cleaned data.
    avg = sum(cleaned) / len(cleaned)
    
    # Step 3: Identify anomalies as values that deviate from the average by more than 10 units.
    anomalies = [x for x in cleaned if abs(x - avg) > 10]
    
    # Step 4: Return a dictionary containing detailed information.
    return {
        "average": avg,
        "anomalies": anomalies,
        "total_data_points": len(data),
        "cleaned_data_points": len(cleaned),
        "anomalies_count": len(anomalies)
    }

if __name__ == "__main__":
    sensor_data = [25, 30, None, 35, 40, 100, 20, None, 15]
    result = process_sensor_data(sensor_data)
    print("Processed Sensor Data:")
    print(f"Average: {result['average']}")
    print(f"Anomalies: {result['anomalies']}")
    print(f"Total Data Points: {result['total_data_points']}")
    print(f"Cleaned Data Points: {result['cleaned_data_points']}")
    print(f"Anomalies Count: {result['anomalies_count']}")