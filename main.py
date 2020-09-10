# -*- coding: utf-8 -*-
"""
Tarea 1 - INF331
"""

from datetime import datetime

def compareStrings(a, b):
    time = datetime.now()
    if(len(a) > len(b)):
        res = a
    elif(len(a) == len(b)):
        res = "Son del mismo largo"
    else:
        res = b
    f = open('logs.txt','a')
    f.write(str(time)+'    a:'+ str(a) + '    b:' + str(b) + '    resultado:' 
            + str(res) + '\n')
    f.close()
    return res


stringA = str(input('Ingrese string A: '))
stringB = str(input('Ingrese string B: '))

res = compareStrings(stringA, stringB)

print('La cadena más larga es: ', res)