import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
rand_letter = ''
for letter in range(0,nr_letters):
    rand = random.choice('letters')
    rand_letter += str(rand)
rand_numbers = ''
for number in range(0,nr_numbers):
    num = random.randint(0,len(numbers)-1)
    rand_numbers += numbers[num]
rand_symbols = ''
for symbol in range(0,nr_symbols):
    sym = random.randint(0,len(symbols)-1)
    rand_symbols += symbols[sym]
randomlist = rand_letter + rand_numbers + rand_symbols
password = ''.join(random.sample(randomlist,len(randomlist)))
print(password)

