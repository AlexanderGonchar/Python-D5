# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def Compression(text): # алгоритм сжатия
    compresdata = ''

    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        compresdata += str(count) + text[i]
        i += 1
    
    return compresdata


def Recovery(text): # алгоритм восстановления
    datarecovery = ''

    i = 0
    while i < len(text):
        datarecovery += str(text[i+1]) * int(text[i])
        i+=2
    
    return datarecovery


with open('Text1.txt', 'r') as t1: # открытие исходного файла
    t1 = t1.read()    

with open('Text2.txt', 'w+') as t2: # запись сжатого файла
    t2.write(Compression(t1))
    t2.seek(0)                     
    t2 = t2.read()
 
with open('Text3.txt', 'w') as t3: # открытие восстановленного исходного файла 
    t3.write(Recovery(t2))