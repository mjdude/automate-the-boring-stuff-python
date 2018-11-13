allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBought(guest, item):
    totalItem = 0
    for k,v in guest.items():
        totalItem += v.get(item,0)
    return totalItem

print('apples bought: ' + str(totalBought(allGuests, 'apples')))
        