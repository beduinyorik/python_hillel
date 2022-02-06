# mylist = ['apple', 'banana', 'cherry']
# print(len(mylist))
#
# string = 'Hello'
# print(len(string))
#
#
# d = {'a': 1, 'b': 1, 'c': 1, 'd': 1}
# keys = list(d)
# print(len(keys))

# mystr = "Привет Python!"
# underline = '-' * len(mystr)
# print(f'{underline}\n{mystr}\n{underline}')

#
#
# new_list = [0, 1, 2, 3, 4]
# print(type(new_list))
# for number in new_list:
#     print(number)
#
# # ==================================
# import random, time
# print(time.time())
# time.sleep(5)
# print(time.time())
# print(random.random(3,9))
# print(len(list(range(100,1 , -1))))


# for num in range(1,100,20):
# # # for num in range(5):
# for num in range(5):
#     if num == 3:
#         print(num)
#         break
#     else:
#         print(num)
# else:
#     print("Числа закончились")

# import asynco as as
# as.

# ==================================
# for num in range(5):
#     if num ==3:
#         break
#     else:
#         print(num)
# else:
#     print("Числа закончились")
# # ==================================
#
# for num in range(5):
#     if num == 3:
#         continue
#     else:
#         print(num)
# else:
#     print("Числа закончились")

# ====================================
# i = 0
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("Конец")
# # ====================================
# i = 0
# while i < 5:
#     if i == 3:
#         break
#     else:
#         print(i)
#         i += 1
# else:
#     print("Конец")
# # ====================================
# i = 0
# while i < 5:
#     if i == 3:
#         i += 1
#         continue
#
#     else:
#         print(i)
#     i += 1
# else:
#     print("Conec")
    # if i == 3:
#         continue
#     else:
#         print(i)
#         i += 1
# else:
#     print("Конец")

# import time
#
# end_time = time.time() + 20
#
# while time.time() < end_time:
#     print("Ok lets wait 5sec")
#     time.sleep(5)
# else:
#     print("Alarm")

# def function_1(name_1="Hello"):
#     return  name_1
#
# print(function_1("Privet"))

def generator(rang):
    for num in range(rang):
        yield num


generator(10)