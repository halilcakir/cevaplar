liste = [3, None,2 ,None,None,1,False,False,10] 


def degistir(liste):
    for i in range(1,len(liste)):
        if liste[i] == None:
            liste[i] =liste[i-1]
    return print(liste)


degistir(liste)