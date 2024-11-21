import random

def sprawdz_pogode():
    pogoda = random.choice(["Pada", "Nie pada"])
    while True:
        odpowiedz = input("Czy pada? (Podaj 'tak' lub 'nie'): ").strip().lower()
        if odpowiedz == "tak" and pogoda == "Pada":
            print("Brawo! Zgadłeś!")
            break
        elif odpowiedz == "nie" and pogoda == "Nie pada":
            print("Brawo! Zgadłeś!")
            break
        else:
            print("Błąd! Spróbuj ponownie.")


sprawdz_pogode()
