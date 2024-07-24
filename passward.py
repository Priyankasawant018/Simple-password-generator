import random
import string

def generate_password(length=12):
    # Define a string containing all possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Use random.choice to select 'length' number of characters from 'characters'
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Example usage:
generated_password = generate_password()
print("Generated Password:", generated_password)
