import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

#niestety nie udało mi się stworzyć logowania do pliku, za kazdym razem wyskakuje mi błąd. Poproszę o wskazówkę? :)

print("Witaj w programie KAKLULATOR\n")

def dodawanie(a, b):
    return a + b
def odejmowanie(a, b):
    return a - b
def mnozenie(a, b):
    return a * b
def dzielenie(a, b):
    return a / b

while True:
    dzialanie = input("Wprowadź odpowiednią liczbę, aby wykonać działanie:\n1 - Dodawanie\n2 - Odejmowanie\n3 - Mnożenie\n4 - Dzielenie\n0 - Zamknij program\n\n")

    if dzialanie in ("1", "2", "3", "4", "0"):
        print(f"Wybrałeś", dzialanie)
        if dzialanie == "0":
            print("Zamykam program")
            break

        liczba1 = float(input("Podaj pierwszą liczbę: "))
        liczba2 = float(input("Podaj drugą liczbę: "))

        if dzialanie == "1":
            print(f"Dodaję: ", liczba1, "+", liczba2)
            print(f"Wynik dodawania:",dodawanie(liczba1, liczba2))
        elif dzialanie == "2":
            print(f"Odejmuję: ", liczba1, "-", liczba2)
            print(f"Wynik odejmowania:",odejmowanie(liczba1, liczba2))
        elif dzialanie == "3":
            print(f"Mnozę: ", liczba1, "*", liczba2)
            print(f"Wynik mnozenia:",mnozenie(liczba1, liczba2))
        elif dzialanie == "4":
            print(f"Dzielę: ", liczba1, "/", liczba2)
            print(f"Wynik Dzielenia:",dzielenie(liczba1, liczba2))

        ponownie = input("Chcesz wykonać inne działanie? (tak/nie): ")
        if ponownie == "nie":
            break
    
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")