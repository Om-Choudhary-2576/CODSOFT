import random
import string

def generate_pass():
    
    
    try:
        
        length = int(input("Enter the desired length of the password: "))
        
        if length < 4:
            print("To be safe, please choose a length of at least 4.")
            return

        
        all_chars = string.ascii_letters + string.digits + string.punctuation
        
       
        password = "".join(random.choice(all_chars) for i in range(length))
        
        print(f"\nYour secure password is: {password}")
        
    except ValueError:
        print("Invalid input! Please enter a number for the length.")


generate_pass()