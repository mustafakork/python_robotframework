name='Mustafa'
surname=' Korkat'
age=36

deneme='My name is '

tanıtmaCümlesi =deneme + ' \n' + name+ surname + '\n and \nI am  ' + str(age)+ ' years old '
length= len(tanıtmaCümlesi)
print(tanıtmaCümlesi)

print(tanıtmaCümlesi[0])
print(tanıtmaCümlesi[3])
print(len(tanıtmaCümlesi))
print(tanıtmaCümlesi.join("M"))
print(tanıtmaCümlesi[length-3])
print(tanıtmaCümlesi[0:6])  #My nam
print(tanıtmaCümlesi[:6])   #My nam
print(tanıtmaCümlesi[0:6:2]) # M a

