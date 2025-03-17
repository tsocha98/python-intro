# Tworzenie dwóch list i ich łączenie funkcją zip()
#Funkcja zip() łączy elementy z dwóch lub więcej iterowalnych obiektów (np. list, krotek) w pary. Zwraca iterator, który można przekonwertować na listę lub inny typ danych.
#https://docs.python.org/3/library/functions.html#zip
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print("Połączone listy:", zipped)

# Użycie funkcji sqrt() z modułu math
# Moduł math zawiera funkcje matematyczne, takie jak pierwiastkowanie, potęgowanie, funkcje trygonometryczne i stałe matematyczne (np. pi, e).
#https://docs.python.org/3/library/math.html
import math
print("Pierwiastek kwadratowy z 16:", math.sqrt(16))

# Obsługa wyjątku ZeroDivisionError
#Wyjątek ZeroDivisionError występuje, gdy próbujemy podzielić liczbę przez zero.
#https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Błąd: Dzielenie przez zero!")