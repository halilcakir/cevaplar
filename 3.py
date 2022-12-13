
palindrom_sayilar = []

def palindrom(): 

   for i in range(100,998):
      carpim=i*(i+1)

      if str(carpim) == str(carpim)[::-1]:
         palindrom_sayilar.append(carpim)
         
   return print(palindrom_sayilar)

palindrom()
