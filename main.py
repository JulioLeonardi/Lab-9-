from encoder import encoder
from encoder import decoder

menu = "Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n"

decoded = ""
encoded = ""

if __name__ == "__main__":
    while True:
        print(menu)
        usel = input("Please enter an option: ")
        if usel == "1":
            password_to_encode = input("Please enter your password to encode: ")
            encoded = encoder(password_to_encode)
            print("Your password has been encoded and stored!\n")
        elif usel == "2":
            decoded = decoder(encoded)
            print(f"The encoded password is {encoded}, and the orignal password is {decoded}\n")
        elif usel == "3":
            break




