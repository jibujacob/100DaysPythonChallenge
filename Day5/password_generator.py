#Password Generator
#Pre-requisites
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def retrieve_list(list,number_of_items):
    output_list=[]
    if (number_of_items>0):
        for i in range(1,number_of_items+1):
            output_list.append(list[random.randint(0,len(list)-1)])
    print(output_list)
    return output_list


print("Welcome to the PyPassword Generator")
number_of_letters=int(input("How many letters would you like in your password?\n"))
number_of_symbols=int(input("How many symbols would you like?\n"))
number_of_integers=int(input("How many numbers would you like?\n"))

symbol_list=retrieve_list(symbols,number_of_symbols)
number_list=retrieve_list(numbers,number_of_integers)
character_list=retrieve_list(letters,(number_of_letters-number_of_symbols-number_of_integers))

password_list=[]
character_list.extend(symbol_list)
character_list.extend(number_list)

random.shuffle(character_list)
password=""
for i in character_list:
    password+=i
print(f"Here is your password: {password}")
