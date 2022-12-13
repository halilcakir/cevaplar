def toplam_fibonacci():
    dizi= [0,1]
    toplam = 0
    i=0
    while True:
    
      toplam =dizi[i] + dizi[i+1]
      dizi.append(toplam)
      i+=1
      if toplam>4000000:
        dizi.pop()
        break

    return print(toplam)

toplam_fibonacci() 
