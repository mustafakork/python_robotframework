name='Mustafa'
surname="Korkat"
age=36

print(f'My name is {name} {surname}') #My name is Mustafa Korkat yazar

print('my name is {0}   {1}'.format(name,surname))  #my name is Mustafa   Korkat
print('my name is {1}   {0}'.format(name,surname))  #my name is Korkat   Mustafa
print('my name is {s}   {n} I am {a} years old '.format(n=name,s=surname, a=age))#My name is Mustafa  Korkat I am 36 years old
print('my name is {} {} I am {} years old '.format(name,surname, age))
print('my name is {} {} I am {} years old '.format(name,name,name))#my name is Mustafa Mustafa I am Mustafa years old
print(f'My name is {name}  {surname} I am {age} years old') #My name is Mustafa  Korkat I am 36 years old


result=200/700
print
print(f'işlem sonucu {result:1.4}')#işlem sonucu 0.2857
print('işlem diğer sonucu {r}'.format(r=result))#işlem diğer sonucu 0.2857142857142857
print('işlem diğer sonucu {r:5.5}'.format(r=result))#işlem diğer sonucu 0.28571
