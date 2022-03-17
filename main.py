from random import randrange

nb1 = randrange(0,10)
nb2 = randrange(0,10)
rep = nb2+nb2
myrep = int(input(f"{nb1} + {nb2} = "))

if myrep == rep:
 print("you win")
else:
 print("you lose")
