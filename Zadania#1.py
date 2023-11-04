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
# 3sposób
print("3 {} {}".format(witaj, imie))
# 4sposób
print("4 %s %s" % (witaj, imie))

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

# zmiana sposobu wyswietlania zmiennr

n = 109.2345654324
print(f"{n:.3f}")

procent = 0.71
print(f"{procent:.1%}")

# %%

variable = "math"
print(f"Using Numeric {variable }")
print(f"|{variable:25}|")
print(f"|{variable:<25}|")
print(f"|{variable:>25}|")
print(f"|{variable:^25}|")

print(f"Using Numeric {variable }")
print(f"|{variable:=<25}|")
print(f"|{variable:=>25}|")
print(f"|{variable:=^25}|")

grd = 10
print(f"This prints without formatting {grd}")
print(f"This prints with formatting {grd:20d}")
print(f"This prints also with formatting {grd:10n}")
print(f"This prints with spacing {grd:10d}\n")
print(f"This prints with formatting {grd:f}")
# %%
# Napisy w Pythonie
napis = "Hello World!"
napis[0]
napis[1]
napis[2]
napis[3]
napis[4]
# ostatnia wartość:
napis[-1]
# pokazije liczbę znaków w napisie len()
sentence = "Lorem ipsum ka jdi klalps"
print(len(sentence))
sentence[24]

# funkcja .index()
hello = "hello, World!"
print(hello.index(" "))

# funkcja .count()
print(hello.count("e"))

# cięcie napisów, odwracanie i tp.
# napis([start:end:step])
print(napis[7:12])
# co drugi
print(napis[::2])
# odwracanie
print(napis[::-1])
print(napis[4::-1])

# .upper() - większe litery
# .lower() - małe litery


# %%

# 18
print("Zadanie 18")
napis01 = "It's always darkest before dawn."
print(napis01)
answer = napis01[0] + napis01[1] + napis01[-1]
print(answer)
answer_v2 = napis01[0:2] + napis01[-1]
print(answer_v2)

# 19
print("Zadanie 19")
print(napis01.replace(".", "!"))


# 20
print("Zadanie 20")
napis02 = "EWERY Strike Brings Me Close to the Next Home run."
print(napis02)
napis02 = napis02.lower()
print(napis02)

# 21
print("Zadanie 21")
napis03 = "don't stop me now."
print(napis03)
napis03 = napis03.upper()
print(napis03)

# 21
print("Zadanie 22")
napis04 = "there are no traffic jams along the extra mile."
print(napis04)
# 1sposób
anw01 = napis[0] == "A"
print(anw01)
# 2sposób
anw2 = napis.
