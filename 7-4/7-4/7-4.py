import math

def quadratic_equation(a, b, c):
    x = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    y = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    return x, y

print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)
