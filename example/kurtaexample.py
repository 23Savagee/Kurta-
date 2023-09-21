def suma(a, b):
    resultado = a + b
    return resultado

def resta(a, b):
    resultado = a - b
    return resultado

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

operacion = input("Seleccione una operación (+ o -): ")

if operacion == "+":
    resultado = suma(num1, num2)
    print(f"La suma de {num1} y {num2} es igual a {resultado}")
elif operacion == "-":
    resultado = resta(num1, num2)
    print(f"La resta de {num1} y {num2} es igual a {resultado}")
else:
    print("Operación no válida")
