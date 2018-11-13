while True:
    print('What is your age?')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age')

while True:
    print('What is your password')
    password = input()
    if password.isalnum():
        break
    print('Please enter an alphanumberic password')