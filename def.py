from random import *
s=nol=pos=neg=[]
def arvud_loendis():
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:
       mini,maxi=vahetus(mini,maxi)
    generaator(n, s, mini, maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    jagamine(s,pos,neg,nol)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",nol)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    s.sort()
    print(s)
                                                                                        
def vahetus(a:int,b:int):
    """Kui a>b, siis vahetame neid
    :param b: Arv, mis on suurem kui b
    :param a: Arv, mis on väiksem kui a
    :rtype:int, int
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """
    :param int n: mittu numbrid genereerib list
    :param n: Mitu täisarvetu
    :param a: Mis on suurem kui b
    :param b:  mis on väiksem kui a
    :rtype:int,list,int,int
    """
    for i in range(n):
        loend.append(randint(a,b))
    

def jagamine(loend:list,p:int,nint,nol:list):
    """
    :param list.loend:
    :param p int: positiivne numbridega kui
    :param n int: negatiivea numbridega kui
    :param nol list: nullige kui
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend:list)->int:
    """
    :param loend.list: numbridega list
    :rtype: list
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
            kesk=round(sum/n,2)
    return kesk

def lisamine(loend:list,el:int)->list:
    """
    :param loend list: number list
    :param el int: numbrid
    :rtype: list: int
    """
    loend.append(el)
    loend.sort()

arvud_loendis()
