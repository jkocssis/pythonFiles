import re

def cpf(texto): #137.889.048-52
    if len(texto) != 14:
        return False
    for i in range(0,3):
        if not texto[i].isdecimal():
            return False
        if texto[3] != '.':
                return False
    for i in range(4,7):
        if not texto[i].isdecimal():
            return False
        if texto[7] != '.':
                return False
    for i in range(8,11):
        if not texto[i].isdecimal():
            return False
        if texto[11] != '-':
                return False
    for i in range(12,14):
        if not texto[i].isdecimal():
            return False
        return True
    
    
text = '137.889.048-52'
print(cpf(text))