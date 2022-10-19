import random
level = input("Easy, medium or hard.")

if level == "easy":
  rnum = random.randint(1,10)
  guess=0
  while guess!=rnum:
        guess=int(input("Enter a random number between 1 to 10:"))
        if  guess<rnum:
            print("Too low!")
            print()
        elif guess>rnum:
            print("Too high!")
            print()
        if guess == rnum:
          print("You have guessed the correct number!")


if level == "medium":
 rnum = random.randint(1,50)
 guess=0
 while guess!=rnum:
        guess=int(input("Enter a random number between 1 to 50:"))
        if  guess<rnum:
            print("Too low!")
            print()
        elif guess>rnum:
            print("Too high!")
            print()
        if guess == rnum: 
          print("You have guessed the correct number!")

          

if level == "hard":
 rnum = random.randint(1,100)
 guess=0
 while guess!=rnum:
        guess=int(input("Enter a random number between 1 to 100:"))
        if  guess<rnum:
            print("Too low!")
            print()
        elif guess>rnum:
            print("Too high!")
            print()
        if guess == rnum: 
          print("You have guessed the correct number!")
