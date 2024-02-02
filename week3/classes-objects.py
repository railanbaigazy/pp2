# Create class My_shape with params color(String) and is_filled (boolean)
# create __init__() method with default values for color and is_filled (choose your own default values)
# override __str__() method (choose your own logic of string generating which includes inner fields values)
# create method getArea() which returns 0;
# Create child classes Rectangle and Circle which extend My_shape class
# add extra fields for Rectangle (x_top_left, y_top_left, length, width)
# add extra fields for Circle (x_center, y_center, radius)
# in each if Rectangle and Circle override method getArea() based on length and width of Rectangle, and radius of Circle
# override __str__() method (add extra fields to reslting string)
# Create a console input for Rectangle creation, and output it with all its fields included in the output.

class MyShape:
    def __init__(self, color="orange", is_filled=False):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        return f"Color: {self.color}, Filled: {'Yes' if self.is_filled else 'No'}"

    def getArea(self):
        return 0

class Rectangle(MyShape):
    def __init__(self, color="black", is_filled=True, x_top_left=0, y_top_left=0, length=0, width=0):
        super().__init__(color, is_filled)
        self.x_top_left, self.y_top_left, self.length, self.width = x_top_left, y_top_left, length, width

    def __str__(self):
        return f"Rectangle. {super().__str__()}, X Top Left: {self.x_top_left}, Y Top Left: {self.y_top_left}, Length: {self.length}, Width: {self.width}"

    def getArea(self):
        return self.length * self.width

class Circle(MyShape):
    def __init__(self, color="black", is_filled=True, x_center=0, y_center=0, radius=0):
        super().__init__(color, is_filled)
        self.x_center, self.y_center, self.radius = x_center, y_center, radius

    def __str__(self):
        return f"Circle. {super().__str__()}, X Center: {self.x_center}, Y Center: {self.y_center}, Radius: {self.radius}"

    def getArea(self):
        import math
        return math.pi * self.radius**2

def create_shape(shape_type):
    color = input("Color: ")
    is_filled = input("Filled? (y)/(n): ").lower() == "y"
    if shape_type == "rectangle":
        params = map(int, input("X Top Left, Y Top Left, Length, Width (comma-separated integers): ").split(','))
        return Rectangle(color, is_filled, *params)
    elif shape_type == "circle":
        params = map(int, input("X Center, Y Center, Radius (comma-separated integers): ").split(','))
        return Circle(color, is_filled, *params)

shapes_name = {
    "r": "Rectangle",
    "c": "Circle",
}

shape_choice = input("What shape do you want to create: Rectangle (r), Circle (c): ").lower()

if shape_choice in shapes_name:
    shape = create_shape("rectangle" if shape_choice == "r" else "circle")
    print(f"\nShape {shapes_name[shape_choice]} was successfully created. Here are its parameters: ")
    print(shape)

    area_command = input("\nIf you want to know the area of your shape, type 'area': ")
    if area_command == "area":
        print(f"Area: {shape.getArea()}")
else:
    print("Invalid choice. Please choose either 'r' or 'c'.")

