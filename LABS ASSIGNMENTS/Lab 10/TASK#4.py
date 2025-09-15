def print_area(shape, **kwargs):
    print(f"Area of {shape}:")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
    print()


def calculate_rectangle_area(length, width):
    area = length * width
    print_area("Rectangle", length=length, width=width, area=area)


def calculate_circle_area(radius):
    area = 3.14 * radius * radius
    print_area("Circle", radius=radius, area=area)


# Example usage
calculate_rectangle_area(10, 5)
calculate_circle_area(7)