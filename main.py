# word = input("Напишите слово")
# if word == "python":
#     print("ДА")
# else:
#     print("НЕТ")
#
#
# slovo1, slovo2 = input(), input()
# if slovo1 == "Да" and slovo2 == "Да":
#     print("ВЕРНО")
# elif slovo2 == "Нет" and slovo1 == "Нет":
#     print("ВЕРНО")
# else:
#     print("НЕВЕРНО")
#
#
# one, two, three = input(), input(), input()
# if one == "раз" and two == "два" and three == "три":
#     print("ГОРИ")
# elif one == "1" and two == "2" and three == "3":
#     print("ГОРИ")
# else:
#     print("НЕ ГОРИ")
#
#
#
# city1, city2 = input(), input()
# if city1 == "Тула" or city2 == "Пенза":
#     print("ДА")
# else:
#     print("НЕТ")
#
#
# n, m = int(input("Введите расстояние")), int(input("Введите кол-во км за день"))
# day = n // m
# print("На день :", day, "он добежит до финиша")
#
#
# road = int(input())
# if ((road // 100 % 100) + (road % 10)) % 8 != 0 and road // 10 % 10 == 3:
#     print("Да")
# else:
#     print(road // 100 % 100 + road % 10, road //10 % 10)
#
#
# tovars = input("Категория:")
# if tovars == "продукты":
#     print("Цена:")
# else:
#     print("Загляните в товары для дома!")
# sell = int(input())
# if sell < 100:
#     print("Попробуйте нашу выпечку!")
# elif sell > 500:
#     print("Попробуйте экзотические фрукты")
# else:
#     print("как начсет орехов в шоколаде?")
#
#
# first, second, third= float(input("Цена первого товара:")), float(input("Цена второго товара:")), float(input("Цена третьего товара:"))
# if first > second and second > third:
#     itogo = (first + second + third) / 3
#     print("Акция!")
#     print("К оплате:", itogo)
# elif first < second and second < third:
#     itogo = (first + second + third) / 2
#     print("Акция!")
#     print("К оплате:", itogo)
# else:
#     itogo = first + second + third
#     print("К оплате:", itogo)
#
#
# yesterday2, yesterday1 = int(input("Введите число покупателей за позавчера:")), int(input("Введите число покупателей за вчера:"))
# if yesterday2 < yesterday1:
#     today = yesterday1 + (yesterday1 - yesterday2)
#     print("Сегодня магазин посетит:", today)
# else:
#     today = yesterday1 - (yesterday1 - yesterday2)
#     print("Сегодня магазин посетит:", today)
#
#
# year = int(input("Введите год:"))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("Год високосный")
# else:
#     print("Год невисокосный")
#
#
# number = int(input())
# if number % 2 == 0:
#     print(number ** 2)
# else:
#     print("число нечетное")
