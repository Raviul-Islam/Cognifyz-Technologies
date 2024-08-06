def main():
    try:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    operator = input("Enter an operator (+,-,*,/,%): ").strip()

    if operator == '+':
        result = n1 + n2
        
    elif operator == '-':
        result = n1 - n2
        
    elif operator == '*':
        result = n1 * n2
        
    elif operator == '/':
        if n2 !=0:
            result = n1 / n2
        else:
            print("Error! Division by 0 is not possible.")
            
    elif operator == '%':
        if n2!=0:
            result = n1 % n2
        else:
            print("Error! Division by 0 is not possible.")
            
    else:
        print("Invalid operator. Enter +,-,*,/,%.")
        return

    print(result)
    
if __name__=="__main__":
    main()