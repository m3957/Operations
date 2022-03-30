def menu():
    print("""
    Opérations
    --------------Ver. 0.3--
    1. Jouer
    2. Info
    3. Quitter
    """)
    menu_input = (input()
    if menu_input == "1":
        #jeu()
    else:
        if menu_input == "2":
            #info()
        else:
            if menu_input == "3":
                print("Bye!")
                quit()
            else:
                print("Erreur. Non valide.")
                # Normalement, je mettrais un int, mais je préfère garder
                # cela comme ça, pour que les voyous qui tapent n'importe
                # quoi ne font pas chnouter tout le programme avec un
                # code d'erreur que machin machin base 10 machin machin.
                print("Est-ce que vous faites exprès?")
                quit() # Un game loop serrait bien, mais ça va être pour plus tard...
        