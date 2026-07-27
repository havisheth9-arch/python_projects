secret = 27  
attempts = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 50.")
print("You have 5 attempts to guess it. Good luck!\n")

while attempts > 0:
    guess = int(input(f"Enter your guess (Attempts left: {attempts}): "))
    
    if guess == secret:
        print(f"🎉 Congratulations! You guessed the secret number {secret} correctly!")
        break
    else:
        attempts = attempts - 1
        difference = abs(guess - secret)
        
        if difference <= 2:
            print("Hint: 🔥 Hot! You are incredibly close!")
        elif difference <= 5:
            print("Hint: 🌡️ Warm! You are getting closer.")
        elif difference <= 12:
            print("Hint: 🥶 Cold! You are far away.")
        else:
            print("Hint: 🧊 Ice Cold! You are nowhere near it.")
        
        if attempts > 0:
            print("Remaining lives: ", end="")
            for i in range(attempts):
                print("❤️", end=" ")
            print("\n" + "-"*30)

if attempts == 0:
    print("\n😢 Game Over! You've run out of attempts.")
    print(f"The secret number was: {secret}")