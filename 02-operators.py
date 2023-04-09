# Operadores test py

x = 3
print(x) # 3

# Sumas y restas
x += 5
print(x) # 8

# Multiplicaciones y divisiones
y = x
y *= 2
print(y, type(y)) # 16 int
y /= 3
print(y, type(y)) # 5.333 float
y %= 3
print(y, type(y)) # 2.333 float
print(10 // 3, type(10 // 3)) # floor division, no tiene en cuenta el resto

# Potencias
print(2 ** 3) # 8 int

#print("Hola " + 5) error! No se pueden mezclar tipos
print("Hola " + str(5)) # error! No se pueden mezclar tipos