users = ['Howard', 'Carrie', 'Wade']
print('Kobe' in users)

subject = '$$$ Get rich now $$$'
print('$$$' in subject)

numbers = [100, 34, 678]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(max(2, 9, 5))

database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843']
]

username = input("User Name: ")
pin = input("PIN code: ")
if [username, pin] in database:
    print('Access granted')

