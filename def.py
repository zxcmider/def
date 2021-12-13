def Pindala(külg1:float,külg2:float)->float:
    """Riistküliku pindala leidmine
    :param float külg1:Riisküliku esimene külg
    :param float külg2:Riistküliku teine külg
    :rtype:float
    """

    S=külg1*külg2
    return S

from Module import *
a=20.5
b=10.75
#S=Pindala(a,b)
S=Pindala(float(input("a")),float(input("b")))
print(S)