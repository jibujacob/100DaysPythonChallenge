#Caesars Challenge
import ceasar_logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
proceed = True
print(ceasar_logo.logo)


while(proceed):
    user_input=input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    message=input("Type your message: \n").lower()
    shift=int(input("Type the shift number: \n"))
    coded_msg=""

    if (user_input=="encode"):
        for letter in range(len(message)):
            temp=message[letter]
            if temp in alphabet:
                asclet=ord(temp)
                temp = chr(97+((asclet+shift-97)%26))
                coded_msg+=temp
            else:
                coded_msg+=temp

        print(f"Here's the encoded result: {coded_msg}")
    else:
        for letter in range(len(message)):
            temp=message[letter]
            if temp in alphabet:
                asclet=ord(temp)
                temp = chr(97+((asclet-shift-97)%26))
                coded_msg+=temp
            else:
                coded_msg+=temp

        print(f"Here's the decoded result: {coded_msg}")

    user_proceed=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if user_proceed != "yes":
        proceed=False

print("Good Bye!")
    