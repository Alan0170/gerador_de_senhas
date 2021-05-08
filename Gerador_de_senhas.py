import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("*" * 31)
print("Bem vindo ao Gerador de senhas!")
print("*" * 31)
nr_letters= int(input("Quantas letras você deseja ter na sua senha?\n")) 
nr_symbols = int(input(f"E quantos símbolos?\n"))
nr_numbers = int(input(f"E quantos números?\n"))


password_list = []

for char in range (1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

#Randomizando a ordem dos caracteres escolhidos
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"\nSua senha é: {password}")
