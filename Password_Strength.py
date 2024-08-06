import re

def Password_Strength(password):
    
    criteria = {
        'length': len(password) >= 8,
        'uppercase': re.search(r'[A-Z]', password) is not None,
        'lowercase': re.search(r'[a-z]', password) is not None,
        'digit': re.search(r'\d', password) is not None,
        'special_char': re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    }
    
    score = sum(criteria.values())
    
    if score == 5:
        strength = 'Very Strong'
    elif score == 4:
        strength = 'Strong'
    elif score == 3:
        strength = 'Moderate'
    else:
        strength = 'Weak'
    
    return strength, criteria

password = input("Enter your password: ")
strength, criteria = Password_Strength(password)
print(f"Password Strength: {strength}")