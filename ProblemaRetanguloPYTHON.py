import math

b = float(input("Base do retangulo: "))
h = float(input("Altura do retangulo: "))

area = b * h
perimetro = 2 * (b + h)
diagonal = math.sqrt(b ** 2 + h ** 2)

print(f"AREA = {area:.4f}")
print(f"PERIMETRO = {perimetro:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")

