# 01,12,23 WPROWADZANIE DANYCH

print("ZAdanie 50")
imie = input("Wprowadż imie,ok?: ")
print(f"OK, masz na imie {imie}")

print("ZAdanie 51")
wiek = input("Wprowadż wiek,ok?: ")
print(f"OK, masz {wiek} lat")

# Type INT!!!
print("ZAdanie 52")
wiek_added = int(
    input("Wprowadż swój wiek, ja powiem, ile będziesz miał za 50 lat, ok?: ")
)
print(f"OK, za 50 lat będziesz miał {wiek_added + 50} lat")

print("ZAdanie 53")
days = int(input("Podaj ilość dni: "))

result = days / 365

print(f"{days} dni to {result} lat")


print("Zadanie 54")
exception = True
while exception:
    exception = False
    try:
        miles = float(input("Podaj ilość mil: "))
    except:
        exception = True
        print("Wpisz poprawna warotśc liczbowa")

result = miles * 1.6

print(f"{miles} mil to {result} km")

#iNSTRUKCJE STERUJĄCE
print("Zadanie 55")
nameBond = input("Podaj imie: ")
if nameBond == "Bond":
    print(f"Welcome on board 007!")
else:
    print(f"Cześć, {nameBond}")

# 55 v2
name = input("Podaj imie: ")
#Niezależnie od literek a spacji
x = name.lower()
x = x.strip()
if "bond" in name.lower().strip():
    print("Welcome aboard agent 007.")
else:
    print(f"Hey, {name}")



#56
number = int(input("Podaj liczbe: "))

if number % 2 == 0:
    print("Parzysta!")
else:
    print("Nieparzysta!")

#custom

number = int(input("Podaj liczbe: "))

if number%3 ==0:
    print("Liczba podzielna przez 3")
elif number%2 == 0:
    print("liczba jest podzielna przez 2")
else:
    print("Liczba nie jest podzielna ani przez 3 ani przez 2")


#Pętla

dzielnik = 50
dzielniki= []
while dzielnik >1:
    if number%dzielnik == 0:
        dzielniki.append(dzielnik)
    dzielnik -=1
if dzielniki:
    print(f"Liczba jest podzielna przez {dzielniki[0]}")
else:
    print(f"liczba nie ejst pdozielna przez liczbe mniejsza lub rowna 50")

#Pętla WHILE

n = 1
while n < 6:
    n += 1
    print(n)

#break continue

#FUNKCJA RANGE 5:00 TIme

#%%
# # n = 0
# #
# # while True:
# #     n -= 1
# #     if n == 4:
# #         break
# #     if n == 1:
# #         continue
# #     print(n)
# # print("koniec petli")
#
# animals = ["Dog", "Cat", "Fish"]
# animal_food = ["Dog food", "cat food", "fish food"]
# for index, animal in enumerate(animals):
#     print(animal, index)
#     if animal == "Dog":
#         animal_food[index] = "Premium Dog food"
#
# print(animals)
# print(animal_food)
#
# # for number in range(100, -1, -1):
# #     print(number)

print("Zadanie 57:")
counter = 100
total = 0
while counter >0:
    total += counter
    counter -=1
print(counter)
print(total)