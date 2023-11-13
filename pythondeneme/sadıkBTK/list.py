message= 'merhaba ben mustafa'
print(message[0]) # m yazar  yazıyı liste gibi algılar

my_list=[1,2,3,4,5]
my_list1=['bir',2,True, 5.4]
print(my_list1[3]) # 5.4

print(my_list[2]) # 3


list3=['one','two','three', 'four']
list4=['five','six','seven', 'eight']

numbers=list3+list4
print(numbers)#['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
print(len(numbers))   #  8 çıktısını verir
print(numbers[2]) # three

userA= ['Mustafa', 36]
userB=['Yasir', 12]
users= userA+userB
print(users) #['Mustafa', 36, 'Yasir', 12]

users=[userA, userB]
print(users) #[['Mustafa', 36], ['Yasir', 12]]
print(users[1]) #['Yasir', 12]
print(users[0][0]) #Mustafa
