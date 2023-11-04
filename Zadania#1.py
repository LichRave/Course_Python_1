# 1
print("Zadanie1")
print("Разниц")
print("Позов")

# 2
print("Zadanie2")
my_text = "Hello, World!"
print(my_text)

# 3
print("Zadanie3")
my_text = "Hello, World!"
print(type(my_text))
print(type(-1))
print(type(2.1))
print(type(1))
print(type(-1))

# 4
print("Zadanie4")
glass_of_wather = 3
print("I drank", glass_of_wather, "glasses of water today.")

# 5
print("Zadanie5")
glass_of_wather = 3
glass_of_wather = glass_of_wather + 1
print("I drank", glass_of_wather, "glasses of water today.")

# 6a-d
print("Zadanie 6a CAŁKOWITA")
x = 10
print(type(x))

print("Zadanie 6b ZMIENNOPRZECINKOWA")
zmienna_2 = 3.14
print(type(zmienna_2))

print("Zadanie6c TEKST")
zmienna_3 = "Tekst Test"
print(type(zmienna_3))

print("Zadanie6d Zmiana")
zmienna_2 = 105
print(type(zmienna_2))

print("Zadanie6c LOGICZNE")
x = True
print(type(x))

# 7
print("Zadanie 7")
my_grade = "10"
answer_5 = float(my_grade)
print(type(answer_5))

# 8
print("Zadanie 8")
my_temp = 97.10
answer_6 = int(my_temp)
print(type(answer_6))

# 9
print("Zadanie 9")
my_temp = 97.10678657
answer_7 = round(my_temp, 2)
print(answer_7)

# 10
print("Zadanie 10")
lst = ["red", "green", "blue"]
print(lst)

# 11
print("Zadanie 11")
a = 10
b = 3
result = a / b
print(result)

# 12
print("Zadanie 12")
speed = 750
speed += 100
print(speed)

# 13
print("Zadanie 13")
remainder = 1000 % 400
print(remainder)

# 14
print("Zadanie 14")
p_result = 11111**2
print(p_result)


# 15
print("Zadanie 15")
a = 450
b = 500

is_equal1 = a == b

print(is_equal1)


# 14
print("Zadanie 14")
p_result = 11111**2
print(p_result)

# 15
print("Zadanie 15")
a = 450
b = 500

is_equel = a == b
print(is_equel)

# 16
print("Zadanie 16")
napis = "It's always darkest before dawn."
print(napis)

# 17
print("Zadanie 17")
witaj = "witaj"
imie = "Jozek"
# 1sposób
print(witaj + " " + imie)
# 2sposób
print(witaj, imie)


# Przykład funkcji {end=""}- znak końca linii printu
print("funkcja end=")
print("Coś", end=" ")
print("fajnego")

# %%
# _1 formatowanie stringów w stylu printf
print("formatowanie stringów w stylu printf  %s")
title = "General"
name = "Kenobi"
print("Hello there, %s %s" % (title, name))

# _2 formatowanie i wyswietlanie stringów w stylu str.format()
title = "General"
name = "Kenobi"
print("Hello there, {} {}".format(title, name))

# _3 Interpolacja ciągów f-string
title = "General"
name = "Kenobi"
print(f"Hello there, {title} {name}")

a = 2
b = 7
print(f"{a} razy {b} do potęgi 2 to {(a*b)**2}")

header1 = "Name"
header2 = "Age"
name2 = "John"
age = 22

print(f"|{header1:10}|{header2:10}|")
print("-" * 27)
print(f"|{name2:10}|{str(age):10}|")
# %%

# 19
print("Zadanie 19")
