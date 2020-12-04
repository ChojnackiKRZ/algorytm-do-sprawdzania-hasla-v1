znaki = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', ':', ';', '"', "'", '<', ',', '>', '.', '?', '/']
lista_znakow_hasla = []
b = -1
a = 0

while (True):
    if a == 0:
        haslo = input (f"Podaj haslo skladajace sie z 8 znakow, znaku specjalnego i duzej litery: ")
        b = -1
        if len(haslo) > 7: 
            for i2 in haslo:
                if i2.isupper():
                    for i in haslo:
                        lista_znakow_hasla.append(i)        
                    for i in lista_znakow_hasla:
                        try:
                            b = znaki.index(i)
                        except:        
                            continue
                    if b > -1 and len(haslo) > 7 and i2.isupper():
                        print ("ok")
                        a = 1
                        break
    else:
        break
            
