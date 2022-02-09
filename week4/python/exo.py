import string
alphabet = string.ascii_lowercase
print(alphabet )
Text=[]
user = input("Entrer Votre Message :")
shift = int(input("Quel Shift Voulez-Vous :"))

for letter in user :
    letter_index = alphabet .index(letter)
    letter_encrypt_index = letter_index+shift
    letter_encrypt = alphabet [letter_encrypt_index]
    Text+=letter_encrypt
    print(Text)