message ="Hello there . My Name is Mustafa . Korkat "
message=message.upper()
print(message)
message=message.lower()
print(message)
message=message.capitalize()#Hello there . my name is mustafa . korkat
print(message)

message=message.strip()
print('Strip metodu Baştaki ve sondaki boşlukları'+message)
message=message.split()
print( message)#['Hello', 'there', '.', 'my', 'name', 'is', 'mustafa', '.', 'korkat']
message1 ='merhaba. mustafa korkat. Nasıl gidiyor'
message1=message1.split('.') # ['merhaba', ' mustafa korkat', ' Nasıl gidiyor']noktadan böler
print(message1)#split noktadan böldü'
message=' '.join(message)
print(message)
print(message.find('mustafa'))
print(message.startswith('H'))
print(message.endswith('b'))

print(message.replace('my','you'))
print(message.replace(' ','*').replace('.', '-').replace('is','are'))
