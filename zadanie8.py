import random

def sprawdz_pogode():
    pogoda = random.choice(["Pada", "Nie pada"])
    number = 0
    while True:
        odpowiedz = input("Czy pada? (Podaj 'tak' lub 'nie'): ").strip().lower()
        if odpowiedz == "tak" and pogoda == "Pada":
            print("Brawo! Zgadłeś!")
            break
        elif odpowiedz == "nie" and pogoda == "Nie pada":
            print("Brawo! Zgadłeś!")
            number += 1
            print(number)
        elif odpowiedz == "nie" and pogoda == "Pada":
            print("Bład! Spróbuj ponownie.")
            number += 1
            print(number)
        elif odpowiedz == "nie wiem":
            print("To wyjdź na zewnątrz i się dowiedz")
        else:
            print("Błąd! Spróbuj ponownie.")


sprawdz_pogode()
