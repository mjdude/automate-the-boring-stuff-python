myPets = ['Zohoie', 'Picachu', 'Magikarp', 'Zapdos']

print('Enter name of pet to check')
name = input()
if name in myPets:
    print('We found', name)
else:
    print(name , 'not found')