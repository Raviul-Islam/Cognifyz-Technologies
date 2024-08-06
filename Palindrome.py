string = input("Enter a string: ").lower()

rev = string[::-1]

if string == rev:
    print("Is palindrome.")
    
else:
    print("Not palindrome.")