nbr = int(input("Saisis un nombre, n'importe lequel : "))
print("Dans l'ensemble infini de ℝ, tu as choisi " + str(nbr) + ". Intéressant...")
print("Voici sa table de multiplication de 1 à 10, comme à l'école :")
for x in range(1, 11):
    print(nbr, "×", x, "=", nbr * x)