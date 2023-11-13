'''

Dairenin Alanı   :nr2
Dairenin çevresi =2nr

*yarı çapı verilen dairenin alan ve çevreesini hesaplayınız
'''

r=(input("dairenin yarıçapını giriniz   : "))

if isinstance(r,(int,float)) :
    n=3.14
    alan=n*r*r
    print(alan)
else:
    print("lütfen sayı giriniz")

#cevre=2*n*r
#print(int(cevre))