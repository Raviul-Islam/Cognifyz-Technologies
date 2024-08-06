import random

def main():
    print("Guess the number game")
    number = random.randint(1,100)
    guess = 0
    
    while guess != number:
        try:
            guess = int(input("Enter your guess (between 1 to 100): "))
            
        except ValueError:
            print("Invalid input! Enter a number between 1 to 100")
            continue
        
        if guess < number:
            print("Input number is less")
            
        elif guess > number:
            print("Input number is high") 
            
        else:
            print("Correct Number!")
            
if __name__ == "__main__":
    main()