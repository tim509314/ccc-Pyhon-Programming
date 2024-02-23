class Circle:
    pi = 3.14159
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * self.pi * self.radius

circle1 = Circle(radius=5)
print(f"Area of the circle: {circle1.area():.2f}")
print(f"Circumference of the circle: {circle1.circumference():.2f}")
