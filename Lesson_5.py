# s1 = 'spam"s'
# s2 = "spam’s"
# s3 = r'C:\newt.txt’
# s4 = r'\n\n\\'[:-1]
# s5 = r'\n\n' + '\\'
# s6 = '\\n\\n'
#
# print(s1[6])
# print(s1 + s2)
# print(s1 * 50)
# print(len(s1))
#  print(s1[0]+s1[2]+s1[-2])
# s ='Hello\nWorld'
# ...
# print(s[::3])
# print(s[nagalo:conec:])

# s = 'spameggs'
# print(s[3:5])
# print(s[2:-2])
# print(s[:6])

# print()
# ==============================
# s = 'spam'
# s[1] = 'b'
#

# s = s[0] + 'b' + s[2:]
# print(s)

# s=str(321)
# s2=''
# for letter in range(-(len(s)-1):
#     s2=s2 + s[letter]
# print((s))
#
# print(s2)
# ================================
# import random
#
# print(random.random())
# =================================
# from random import randint, randrange
#
# # print("Вывод случайного целого числа ", randint(0, 9))
# print("Вывод случайного целого числа ", randrange(0, 10, 2))
# # =================================
# import random
#
# city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
# print(city_list[random.randint(0, len(city_list)-1)])
# print("Выбор случайного города из списка - ", random.choice(city_list))
# phase="Выбор случайного города из списка"
# new_phase=phase.split(" ")
# print(type(new_phase))
# print(random.choice(new_phase))
# # =================================
#
# print("Использование random.randint() для генерации случайного целого числа")
# print(random.randint(0, 5))
# print(random.randint(0, 5))
# ==================================
#
# list = [20, 30, 40, 50 ,60, 70, 80, 90]
# sampling = random.choices(list, k=5)
# print("Выборка с методом choices ", sampling)
# print(f"Выборка с методом choices {list_of_numbers}, {list_of_number[0]}, {list_of_number[1]}, {list_of_number[2]}h
# t("Выборка с методом choices ", list)
# # ===================================


# Пишем программу выбора одежды на работу

# closes_list = ['Пиджак', 'Рубашка', 'Футболка', 'Шляпа', 'Брюки', 'Носки', 'Шуба', 'Кепка', 'Тапки', 'Платок', 'Плавки']
# print("Выбор случайной одежды из списка - ", random.choices(closes_list, k=3))

# closes_list = ['Пиджак', 'Рубашка', 'Футболка', 'Шляпа', 'Брюки', 'Носки', 'Шуба', 'Кепка', 'Тапки', 'Платок', 'Плавки']
# print("Выбор случайной одежды из списка - ", random.choices(closes_list, k=3))
#
import random

# print(random.gauss(0.1,1))
# closes_list = ['Пиджак', 'Рубашка', 'Футболка', 'Шляпа', 'Брюки', 'Носки', 'Шуба', 'Кепка', 'Тапки', 'Платок', 'Плавки']
# print("Выбор случайной одежды из списка - ", random.choices(closes_list, k=3))

print(random.gauss(0.1,1))
closes_list = ['Пиджак', 'Рубашка', 'Футболка', 'Шляпа', 'Брюки', 'Носки', 'Шуба', 'Кепка', 'Тапки', 'Платок', 'Плавки']
print("Выбор случайной одежды из списка - ", random.sample(closes_list, k=3))
