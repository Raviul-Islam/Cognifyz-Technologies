import random

def main():
    print("Guess the number game")
    i = int(input("Enter starting number: "))
    j = int(input("Enter ending number: "))
    number = random.randint(i,j)
    guess = 0
    
    while guess != number:
        try:
            guess = int(input("Enter your guess: "))
            
        except ValueError:
            print("Invalid input! Enter a number.")
            continue
        
        if guess < number:
            print("Input number is less")
            
        elif guess > number:
            print("Input number is high") 
            
        else:
            print("Correct Number!")
            
main()