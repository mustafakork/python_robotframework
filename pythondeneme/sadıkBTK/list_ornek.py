aracList=['BMW','Mercedes', 'Mazda','Tofaş']

print(len(aracList)) #4
# 1- listenin ilk ve son elemanı
print(aracList[0]) #
print(aracList[len(aracList)-1])

# 2- Mazdayı toyata ile değiştirin
aracList[2]='toyata'
print(aracList) #['BMW', 'Mercedes', 'toyata', 'Tofaş']
# 3- liste kaç elemanlıdır
print(len(aracList)) # 4 

# 5- mercedes listenin bir elemanı mıdır?

aracList1= 'Mercedes' in aracList
print(aracList1)

# 6- listenin -2 değeri nedir
aracList=aracList[-2]

print(aracList) #toyota

# 7- listenin ilk üç elemanı nedir
aracList=['BMW','Mercedes', 'Mazda','Tofaş']

aracList=aracList[0:3]
aracList=aracList[:3]
print(aracList) #['BMW', 'Mercedes', 'Mazda']
aracList=aracList[-2:]# -2 den sona kadar gider

# 8- listenin son iki elemanı yerine 'reno' ve 'muko' yazılı
# 1. yöntem ayrı ayro
#aracList[-1]= 'reno'  aracList[-2]= 'muko'

#2. yöntem

aracList[-2:]= ['reno', 'muko']

#9- listenin içerisine 'audi ve nissan ekleyeli

aracList=aracList + ['audi', 'nissan']# ['reno', 'muko', 'audi', 'nissan']

# 10 -  listenin son elemanın silin
del aracList[-1] #['reno', 'muko', 'audi'] nisssan silindi
aracList.pop()# ['reno', 'muko']   audi silindi

# 11- listenin elemanlarını tersten yazdıralı 
aracList= aracList[::-1]

# 12 -  örnek liste yapalım

studentA= ['mustafa','Korkat', 1981, [70,80,90]]
studentB= ['Yasir','Korkat', 2012, [80,80,90]]
studentC= ['Yakup','Korkat', 2016, [70,60,90]]

print(studentA)
print(studentB)
print(studentC)

yazı1= f'{studentA[0]} {studentA[1]} {studentB[0]} ve {studentC[0]} nin babasıdır.yasi {2023-studentA[2]} dır'

print(yazı1)
notOr= {studentB[3][0]} 
notOr1= {studentB[3][1]}
notOr2={studentB[3][2]}
notOr3=notOr+notOr2
print(notOr3)


yasirinNotOrtalaması= f' {studentB[0]} {2023-studentB[2]}  yasindadır. not ortalaması   dür'


a=20
b=20

c=(a+b)/2
print(c)















