# -*- coding: utf-8 -*-
"""
Tarea 1 - INF331
"""

from datetime import datetime

def compareStrings(a, b):
    time = datetime.now()
    if(len(a.replace(" ", "")) > len(b.replace(" ", ""))):
        res = a
    elif(len(a.replace(" ", "")) == len(b.replace(" ", ""))):
        res = "Son del mismo largo"
    else:
        res = b
    f = open('logs.txt','a')
    f.write(str(time) + '    a:"'+ str(a) + '"    b:"' + str(b) + '"    resultado:"' 
            + str(res) + '"\n')
    f.close()
    return res
while(True):
    try: 
        stringA = str(input('Ingrese string A: '))
        stringB = str(input('Ingrese string B: '))
        
        res = compareStrings(stringA, stringB)
        
        print('La cadena más larga es: "' + str(res) + '"')
        break
    except KeyboardInterrupt:
        print('\n Interrupción provocada, reiniciando...')
        continue