from random import randrange
from random import choice
bonne_rep = ["Bien!", "Wow!", "Continue comme ça!"]
mauv_rep = ["Tu peux faire mieux!", "Allez!", "Mauvaise réponse, petit bonhomme!"]
operation_nb = 0
nb_operations = int(input("Combien d'opérations? "))
def topbar():
    print(f"========= {operation_nb}/{nb_operations} =========")

def jeu(): # À ajouter plus tard,
    for i in range(nb_operations): # Ne pas utiliser nb_operations mais un machin de def
    nb1 = randrange(0,10)
    nb2 = randrange(0,10)
    rep = nb1+nb2
    topbar()
    myrep = int(input(f"{nb1} + {nb2} = "))
    operation_nb = operation_nb+1
    if myrep == rep:
        print(choice(bonne_rep))
        #print("yes")
    else:
        print(choice(mauv_rep))
        #print("bouh")
        print(f"La bonne réponse était {rep}.")

jeu()
