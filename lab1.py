def z1():
    pas1=input("Введите пароль")
    pas2=input("Введите пароль повторно")

    if len(pas1)> 6 and len(pas2)>6:
        print("пароль надёжный")
    else :
        print("пароль не надёжный")

    if pas1 == pas2:
        print("пароли совпадают")
    else:
        print("пароли не совпадают")

def z2():
    a= int(input("Введите номер вашего места"))
    if a>36:
            print ("ваше место боковое")
    elif a % 2:
        print("ваше место нижнее")
    else:
        print("ваше место верхнее")
def z3():
    a = int(input("Введите год"))
    if (a% 4 == 0) and (a% 100 != 0) or (a% 400 == 0):
        print("год",a,"високосный")
    else:
        print("год",a,"не високосный")

def z4():
    colors=('красный','синий','желтый')
    c1=input()
    c2=input()
    if c1 in colors and c2 in colors:
        if c1!=c2:
            if (c1 in ('красный','синий')) and (c2 in ('красный','синий')):
                print('фиолетовый')
            if (c1 in ('красный','желтый')) and (c2 in ('красный','желтый')):
                print('оранжевый')
            if (c1 in ('синий','желтый')) and (c2 in ('синий','желтый')):
                print('зеленый')
        else:
            print(c1)
    else:
        print('ошибка цвета')


def z5():
    n=int(input('задайте количество слов'))
    A=[0]*n
    for i in range (0,n):
        print('введите слово: ')
        A[i] = input()
        i+=1
    for i in range (0,n):
        print(A[i],end = ' ')
        i+=1

z1()
z2()
z3()
z4()
z5()