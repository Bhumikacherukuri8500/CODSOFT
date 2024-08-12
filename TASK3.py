#password generator
import random
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','_','(',')','+']
print("welcome to password generator")
n_letters=int(input("how many letters you want in password?\n"))
n_symbols=int(input("enter how many symbols you want in password?\n"))
n_numbers=int(input("enter how many numbers you want in password?\n"))
password=""
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password+=char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password+=char
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password+=char
print(password)
