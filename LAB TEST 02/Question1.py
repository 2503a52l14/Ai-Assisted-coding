def calculate_fares(rides, base_per_km, surge_multiplier):
    """
    Calculate fares for a list of rides based on time and distance.

    Args:
        rides (list): List of dictionaries with 'time' (HH:MM) and 'km' (float).
        base_per_km (float): Base rate per kilometer.
        surge_multiplier (float): Multiplier for surge pricing after 18:00.

    Returns:
        list: List of fares rounded to 2 decimal places.
    """
    fares = []
    for ride in rides:
        time = ride['time']
        km = ride['km']

        # Parse the hour and minute from the time string
        hour, minute = map(int, time.split(':'))

        # Determine if surge pricing applies
        if hour > 18 or (hour == 18 and minute > 0):
            fare = km * base_per_km * surge_multiplier
        else:
            fare = km * base_per_km

        # Round the fare to 2 decimal places
        fares.append(round(fare, 2))

    return fares

# Quick test
if __name__ == "__main__":
    rides = [{'time': '08:00', 'km': 3.0}, {'time': '18:30', 'km': 5.0}]
    base_per_km = 12.0
    surge_multiplier = 2.0

    result = calculate_fares(rides, base_per_km, surge_multiplier)
    print(result)  # Expected output: [36.0, 120.0]