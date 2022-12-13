
import re

kelime = 'elma, armut , ?portakal'

def avg_len(kelime):
    
    kelime_listesi = re.split('[,.!?:;]',kelime)
    kelime_listesi.remove(' ')
    toplam=0
    sayac=0
    avg=0
    
    
    for i in range(len(kelime_listesi)):
        toplam += len(kelime_listesi[i])
        if ' ' in kelime_listesi[i]:
            for k in range(len(kelime_listesi[i])):
                if kelime_listesi[i][k] == ' ':
                    sayac +=1
        
    avg=(toplam-sayac)/len(kelime_listesi)
    return print(avg)
    


   


avg_len(kelime)


