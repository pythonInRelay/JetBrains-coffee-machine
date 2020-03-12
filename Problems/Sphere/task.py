class Sphere:
    pi = 3.14

    def __init__(self, radius):
        print(round((4/3 * Sphere.pi * radius ** 3), 2))


rad = float(input())

Sphere(rad)
