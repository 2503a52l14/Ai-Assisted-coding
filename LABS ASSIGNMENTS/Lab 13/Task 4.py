import math

def calculate_circle_properties(radius):
    """
    Calculate the area and circumference of a circle given its radius.

    Parameters:
        radius (float): The radius of the circle.

    Returns:
        dict: A dictionary containing the area and circumference of the circle.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    # Calculate area and circumference
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    return {
        "area": area,
        "circumference": circumference
    }

def main():
    """
    Main function to demonstrate the calculation of circle properties.
    """
    print("Circle Properties Calculator")

    try:
        # Input radius from the user
        radius = float(input("Enter the radius of the circle: "))

        # Calculate properties
        properties = calculate_circle_properties(radius)

        # Display results
        print(f"Area: {properties['area']:.2f}")
        print(f"Circumference: {properties['circumference']:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()