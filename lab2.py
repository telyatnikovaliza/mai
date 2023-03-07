def prog1():
    words=[]
    while (new_word := str(input())) != 'stop':
        words.append(new_word)
        print(' '.join(words))

def prog2():
    words = []
    while (new_word := str(input())) != 'stop':
        if "ф" in new_word or 'Ф' in new_word:
            print('редкое слово')
        else:
            print('не очень редкое слово')

def prog3():
    import random
    k = 0
    while k<3:
        a=random.randit(0,9)
        b = random.randit(0, 9)
        print(a,'+',b,'=')
        res = int(input())
        if res == a + b :
            print('true')
        else:
            print('false')
            k+=1
    else:
        print('game over')

prog1()
prog2()
prog3()