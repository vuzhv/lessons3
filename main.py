# Условна конструкція - ми можемо провірити вираження якщо воно вірне то ми виполним один кусочок кода якщо ні то інший

#user_data = int(input("Введіть число :"))



#if user_data > 5:
#   print("Number is bigger than 5")
#    if user_data == 9:
#       print("Number is 9")
# проверку можна робити на < > >= <= == !=(нерівність)
#головне однакова кількість відступів

#user_data = int(input("Введіть число :"))
#isHappy = False

#if isHappy: #if or if not
#    print("User is happy")
#elif user_data == 5:
#    print("Number is 5")
#elif user_data == 7:
#    print("Number is 7")
#else:
#    print("User is unhappy")

# elif дполонительное условие если оно оказується верное то в таком случае виполняеться його
# код якщо нет то виполняється else
# else виповнлюється якщо не вірне if
#else завжди в самом низу

#user_data = int(input("Введіть число :"))
#isHappy = True
#if isHappy and user_data == 6 or 5 == 5:   #and обєднання двух условий(повинні бути оба правильними)
#    print("User is happy")       #or або, якщо одна із частин буде правильною то виповниться условие
#elif user_data == 5:
#    print("Number is 5")
#elif user_data == 7:
#    print("Number is 7")
#else:
#    print("User is unhappy")

data = input()
number = 5 if data == "Five" else 0 #тернарний оператор if else тільки в одну строку
print(number)

#if data == "Five":
#    number = 5
#else:
#    number = 0
#print(number)









