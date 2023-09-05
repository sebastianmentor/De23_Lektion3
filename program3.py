print('Meny'.center(24,'-'))
print('1. Skriv in namn')
print('2. Skriv in ålder')
print('3. Avsluta')

val = input('Skriv in val: ')
name,age = None,None

if val=='1':
    name = input('Vänligen skriv in ditt namn: ')
elif val == '2':
    age = input('Vänligen skriv in din ålder: ')
elif val == '3':
    print('Vi avslutar programmet! Hej då!')
else:
    print('Kära användare, det verkar som att du inte kan läsa!')

if name != None:
    print('Hej på dig',name)
if age != None:
    if int(age) >= 30:
        print('Du är en gammal jäkel!')