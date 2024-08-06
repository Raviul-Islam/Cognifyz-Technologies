def converter(t,u):
    
    if u == "Celsius":
        print((t*9/5) + 32)
        
    elif u == "Fahrenheit":
        print((t - 32)*5/9)
        
    else:
        print("Invalid input. Press C or F.")
        
t = int(input("Enter temperature: "))
u = input("Enter unit: ")
converter(t,u)