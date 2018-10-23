catNames = []
while True:
    print('Enter the name of cat', len(catNames) + 1 , 'Or enter nothing to stop')
    catName = input()
    if catName != '':
        catNames = catNames + [catName]
    else:
        break
    
print('Cat names are')
for name in catNames:
    print(name)


