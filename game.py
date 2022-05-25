from random import randint

name = input("Hi! What is your name")

month = randint(1,12)

year = randint(1924,2004)

guess = 1

# Guess 1
print("Guess ", guess, ": ", name, " were you born in ", month, " / ", year)
answer = input("yes or no?")

if answer == "yes":
    print("I knew it")
    exit()
elif answer =="no":
    if(guess < 5):
        print("Drat! Lemme try again")
    else:
        print("I have other things to do, Good bye.")
        exit()
    month = randint(1,12)
    year = randint(1924,2004)
    guess = guess + 1

# Guess 2
print("Guess ", guess, ": ", name, " were you born in ", month, " / ", year)
answer = input("yes or no?")

if answer == "yes":
    print("I knew it")
    exit()
elif answer =="no":
    if(guess < 5):
        print("Drat! Lemme try again")
    else:
        print("I have other things to do, Good bye.")
        exit()
    month = randint(1,12)
    year = randint(1924,2004)
    guess = guess + 1

# Guess 3
print("Guess ", guess, ": ", name, " were you born in ", month, " / ", year)
answer = input("yes or no?")

if answer == "yes":
    print("I knew it")
    exit()
elif answer =="no":
    if(guess < 5):
        print("Drat! Lemme try again")
    else:
        print("I have other things to do, Good bye.")
        exit()
    month = randint(1,12)
    year = randint(1924,2004)
    guess = guess + 1

# Guess 4
print("Guess ", guess, ": ", name, " were you born in ", month, " / ", year)
answer = input("yes or no?")

if answer == "yes":
    print("I knew it")
    exit()
elif answer =="no":
    if(guess < 5):
        print("Drat! Lemme try again")
    else:
        print("I have other things to do, Good bye.")
        exit()
    month = randint(1,12)
    year = randint(1924,2004)
    guess = guess + 1

# Guess 5
print("Guess ", guess, ": ", name, " were you born in ", month, " / ", year)
answer = input("yes or no?")

if answer == "yes":
    print("I knew it")
    exit()
elif answer =="no":
    if(guess < 5):
        print("Drat! Lemme try again")
    else:
        print("I have other things to do, Good bye.")
        exit()
    month = randint(1,12)
    year = randint(1924,2004)
    guess = guess + 1

