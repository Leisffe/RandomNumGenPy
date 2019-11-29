import random

wylosowana = random.randrange(1, 101)
#debug print(wylosowana)
iloscprob = 0

print("Proszę podaj liczbę z zakresu 0-100 (Masz tylko 10 prób!): ")

while iloscprob < 10:
    podana=int(input())
    iloscprob=iloscprob+1
    if podana<wylosowana:
        print('Za mała liczba, spróbuj ponownie.')
    if podana>wylosowana:
        print('Za duża liczba, spróbuj ponownie.')
    if podana==wylosowana:
        break
if podana==wylosowana:
    print('Brawo przyjacielu! Udało Ci się zgadnąć po ' +str(iloscprob) + ' próbach!')
else:
    print('Niestety nie udało Ci się odgadnąć liczby :(   Dana liczba to: ' +str(wylosowana))