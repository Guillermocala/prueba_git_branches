def max(num1, num2):
    return (num1 if num1 > num2 else num2)

num1 = int(input("ingresa el num1: "))
num2 = int(input("ingresa el num2: "))
print("el mayor es: ", max(num1, num2))