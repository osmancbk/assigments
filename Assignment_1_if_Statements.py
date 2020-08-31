passwords = {"tarik" : '1234', "ahmet" : '5678', "mehmet" : '9654', "ali" : '98765', "osman" : '3256'}

name = input('Please, enter your name')

if name in passwords.keys():
    print(f'Hello, {name}! The password is : {passwords[name]}')
else:
    print(f'Hello, {name}! See you later.')