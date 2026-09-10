import random
import string

while True:

    length = int(input("ENTER YOUR PASSWORD LENGTH: ")) # taking input length from user 

    characters = string.ascii_letters + string.digits + string.punctuation #including letters,numbers,characters

    password = "".join(random.choice(characters) for _ in range(length)) #genrating random password

    print("\nGenerated Password:", password) #displaying generated password

    choice = input("\nDo you want to generate another password (yes/no): ").lower() #asking user to generate another password 

    if choice != "yes":
        print("THANK YOU FOR USING PASSWORD GENERATOR!") 
        break
