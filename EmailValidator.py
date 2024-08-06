import re

def validator(email):
    
    expression = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(expression, email):
        print("Valid email address.")
    else:
        print("Invalid email address.")

email = input("Enter an email address: ")
validator(email)