while True:
    nbr = int(input("Saisis un nombre entier, n'importe lequel : "))
    print("\nDans l'ensemble infini de ℚ, tu as choisi " + str(nbr) + ". Intéressant...")
    print("Voici sa table de multiplication de 1 à 10, comme à l'école :")
    for x in range(1, 11):
        print(nbr, "×", x, "=", nbr * x)

    while True:
        asw = input("\nVeux-tu essayer avec un autre nombre (oui: o ; non: n) ? ")
        asw = asw.lower()

        if asw == "o":
            break
        elif asw == "n":
            print("Bye.")
            exit()
        else:
            print("Je crois qu'on s'est mal compris.")