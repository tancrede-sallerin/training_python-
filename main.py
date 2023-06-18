import os
import time
import random


def clear_screen():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

# données initiales
nb_initial = []
for i in range(4): nb_initial.append(str(random.randint(0, 9)))
nb_initial = ''.join(nb_initial)

# début
print("retenez la séquence")
time.sleep(1)
print(f"La séquence à mémoriser est: {nb_initial}")
time.sleep(3)


score = 0

while True:
    clear_screen()

    reponse = input('quelle est votre réponse: ')

    if reponse == nb_initial:
        score += 1
        print(f"Bonne réponse, votre score est : {score}")
        time.sleep(1)

    else:
        print(f"Mauvaise réponse, la séquence était : {nb_initial}, votre score final : {score}")
        break

    clear_screen()

    print('retenez la séquence')
    time.sleep(1)

    nb = str(random.randint(0, 9))
    nb_initial = nb_initial + nb
    print(f"La séquence à mémoriser est: {nb_initial}")
    time.sleep(3)


