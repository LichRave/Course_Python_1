# -*- coding: utf-8 -*-

# строковые префикры u и r. u- интерпретатор utf; r - буквальное печатание
print("Привет, мир !")
print("Привет вновь !")
print("Мне нравится это печатать.")
print("Ура, я пеатаю!")
print("Это весело!")
print("Это занятие как 'волшебство'.")
print('Я бы "сказал", что это очень круто!')
# 1
print("Tu coś nowego")

# %%
# what does the program do
print("Я подсчитаю свою живность")
# number of chickens
print("Куры", 25 + 30 / 6)
# number of roosters
print("Петухи", 100 - 25 * 3 % 4)
# number of eggs
print("А теперь подсчитаю яйца:")
# stupid example
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
# question 1
print("Верно ли, что 3+2<5-7")
# answer 1
print(3 + 2 < 5 - 7)
# question 2
print("Сколько будет 3+2?", 3 + 2)
# answer 2
print("А сколько будет 5-7?", 5 - 7)
# doubts
print("Ой, я, кажется, запутался... Почему False?")
# request
print("Еще раз посчитаю...")
# question 3
print("Это больше?", 5 > -2)
# question 4
print("А это больше или равно?", 5 >= -2)
# question 5
print("А это меньше или равно?", 5 <= -2)

# %%
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers

carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("В наличии", cars, "автомобилей")
print("И только ", drivers, "вышло на работу")
print("Получается, что", cars_not_driven, "машин пустует")
print("Мы можем перевести сегодня", carpool_capacity, "человек")
print("В каждой машине будет примерно", average_passengers_per_car, "человека")

# %%
print("FULLBODY")

my_name = "Artem"

print(f"Let's say about a human by name %s.")


# %%
def func(a, b=5, c=10):
    print("a =", a, "| b =", b, "| c =", c)


func(3, 7)
func(25, c=24)
func(c=50, a=100)

# %%
num = 23
guess = int(input("Введите число: "))
if guess == num:
    print("You won!")
elif guess < num:
    print("So close <:")
else:
    print("So close <:")
print("End.")


# %%
def total(a=5, *num, **phonebook):
    print(a)

    for item in num:
        print(num)

    for first, second in phonebook.items():
        print(first, second)


print(total(10, 1, 2, 4, Jack=1223, John=2231, Max=2654))

# %%
