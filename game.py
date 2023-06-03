# Warsztat: Gra w zgadywanie liczb 2
# Odwróćmy teraz sytuację z pierwszego zadania: 
# ("Gra w zgadywanie liczb"). Niech użytkownik pomyśli sobie liczbę z zakresu 1-1000,
# a komputer będzie zgadywał. Zrobi to maksymalnie w 10 ruchach 
# (pod warunkiem, że gracz nie będzie oszukiwał).

# Zadaniem gracza będzie udzielanie odpowiedzi "Too small", "Too big", "You win".

# Do tego warsztatu dołączony jest schemat blokowy algorytmu. 
# Zaimplementuj go w Pythonie.

print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w maks. 10 próbach.")

def guess(min, max):
    return int((max - min)/2 + min)

min = 0
max = 1000
loop = 0

while True:
    loop += 1
    current_guess = guess(min, max)

    print(f"{loop}: Zgaduję {current_guess}")

    answer = input('''
    Napisz "zgadłeś", jeżeli pomyślałeś o tej liczbie.
    Napisz "za dużo", jeżeli pomyslałeś o mniejszej liczbie.
    Napisz "za mało", jeżeli pomyślałeś o większej liczbie.

    ''')

    if answer == "zgadłeś":
        print("Wygrałem!")
        break
    elif answer == "za dużo":
        max = current_guess
    elif answer == "za mało":
        min = current_guess