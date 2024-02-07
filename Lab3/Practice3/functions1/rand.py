import random
name = input("Hello! What is your name? ")
ToGuess = random.randint(1, 20)
def Guess(name, ToGuess):
    cnt = 0
    Number = int(input(f"""Well, {name}, I am thinking of a number between 1 and 20.
Take a guess."""))
    if(Number!=ToGuess): 
        while(Number!=ToGuess):
            Number = int(input("""Your guess is too low.
    Take a guess."""))
            cnt+=1
        print(f"Good job, KBTU! You guessed my number in {cnt} guess!")
    else:
        print("Good job, KBTU! You guessed my number in 1 guess!")
Guess(name, ToGuess)