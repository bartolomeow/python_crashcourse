# Variable test py

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)
print(type(my_int_variable))

my_bool_variable = False
print(my_bool_variable)

my_int_to_string_variable = str(my_int_variable)
print(my_int_to_string_variable)
print(type(my_int_to_string_variable))
# Función ternaria
result = my_int_variable == my_int_to_string_variable and "equal" or "not equal"

print(my_int_variable, "and", my_int_to_string_variable, "are", result)

my_string_variable = "My String variable"
print(my_string_variable, my_int_variable, my_int_to_string_variable, my_bool_variable)

# Funciones del sistema
print(len(my_string_variable))

# Variable en una sola línea
name, surname, alias, edad = "Carlos", "Paqué", "bartolomeow", "99"
print(name, surname, alias, edad)

"""
first_name = input("What's your name? ")
age = input("How old are you? ")

print(first_name,'is',age,'YO')
"""

# ¿Forzado de tipos? Realmente no se queja...
address: str = "My address"
address = 32
print(type(address))
