while True:
    print("Who are you?")
    name = input()
    if name != 'Joe':
        continue
    print('Hello, ' + name + '. What is the password? (Is it a fish?)')
    password = input()

    if password == 'swordfish':
        break
print('Congratulations - Access granted')