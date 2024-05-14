#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# Without shuffle
# letterstr = ""
# numberstr = ""
# symbolstr = ""
# pletters = ""
# pnumbers = ""
# psymbols = ""

# for letter in letters:
#   letterstr += letter
# # print(letterstr)

# for number in numbers:
#   numberstr += number
# # print(numberstr)

# for symbol in symbols:
#   symbolstr += symbol
# # print(symbolstr)

# for pletter in range(0, nr_letters):
#   randomlet = random.randint(0, 51)
#   pletter = letters[randomlet]
#   pletters = pletters + pletter
# # print(pletters)

# for pnumber in range(0, nr_numbers):
#   randomnum = random.randint(0, 9)
#   pnumber = str(numbers[randomnum])
#   pnumbers = str(pnumbers) + pnumber
# # print(pnumbers)

# for psymbol in range(0, nr_symbols):
#   randomsym = random.randint(0, 8)
#   psymbol = str(symbols[randomsym])
#   psymbols = str(psymbols) + psymbol
# # print(psymbols)

# password = pletters + pnumbers + psymbols

# print(f"Here is your password: {password}")

# -------------------------------------With shuffle-----------------------------------------

password_list = []

for char in range(0, nr_letters):
  password_list += random.choice(letters)

for char in range(0, nr_numbers):
  password_list += random.choice(numbers)

for char in range(0, nr_symbols):
  password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Here is your password: {password}")