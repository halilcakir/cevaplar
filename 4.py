def asalsayi_bul():
    asal_sayilar = []
    sayi = 2

    while len(asal_sayilar) < 10001 :
        if sayi > 1:  
            for i in range(2,sayi):  
                if (sayi % i) == 0:  
                    break  
            else:  
                asal_sayilar.append(sayi)

        sayi +=1

    return print(asal_sayilar[10000])

asalsayi_bul()