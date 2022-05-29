# Ici, je teste le code, et regarde si il y a des trucs...
# Je fais cela pour ne pas scrapper le programme original.

from random import randrange
from random import choice
from time import sleep
import webbrowser

global nb_operations
nb_operations = 0
bonne_rep = ["Bien!", "Wow!", "Continue comme ça!", "Nice.", "Continue!", "Go Go Go!"]
mauv_rep = ["Tu peux faire mieux!", "Allez!", "Mauvaise réponse, petit bonhomme!", "Common!"]

operation_nb = 0

def info():
    print("""
    Jeu fait par @m3957 pour apprendre Python.
    Ah? Vous ne savez pas que je suis un
    noob. :D

    Liens utiles:
        Scratch: https://scratch.mit.edu/users/m3957
        Github:  https://github.com/m3957

    Faire Enter pour continuer
    """)
    input() # Enter pour continuer


def topbar(nb_operations):
    print(f"========= {operation_nb+1}/{nb_operations} =========")

def jeu(): # À ajouter plus tard,
    nb_operations = int(input("Combien d'opérations? "))
    if nb_operations == 0:
        print("""
        Comment tu veux coder si tu ne peux pas
        pratiquer tes maths? C'est le but du jeu!

        Fait Enter pour continuer
        """)
        input()
        print("Nous n'avons pas le choix pour toi...")
        sleep(2)
        print("On doit changer quelque chose...")
        webbrowser.open('https://www.youtube.com/watch?v=igcoDFokKzU')
    for i in range(nb_operations): # Ne pas utiliser nb_operations mais un machin de def
        nb1 = randrange(0,10)
        nb2 = randrange(0,10)
        rep = nb1+nb2
        topbar(nb_operations)
        myrep = int(input(f"{nb1} + {nb2} = "))
        global operation_nb
        operation_nb = +1
        if myrep == rep:
            print(choice(bonne_rep))
            #print("yes")
        else:
            print(choice(mauv_rep))
            #print("bouh")
            print(f"La bonne réponse était {rep}.")

#Bouuuuuh!! Le gros code de menu!!! Tellement épeurant!! Bouuuuuuuuuh!!!!
def menu():
    print("""
    Opérations
    --------------Ver. 0.3--
    1. Jouer
    2. Info
    3. Quitter
    """)
    menu_input = input()
    if menu_input == "1":
        jeu()
    else:
        if menu_input == "2":
            info()
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


menu()