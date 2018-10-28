birthdays = {'Alive' : 'Apr 1', 'Bob': 'Dec 12', 'Carol' : 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    
    if name in birthdays:
        print(birthdays[name] , 'is the birthday of', name)
    else:
        print('Cannot find' , name, 'please enter their birthday')
        date = input()
        birthdays[name] = date
        print('Database updated with birthday for', name)
        print(birthdays)
