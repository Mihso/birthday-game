from random import randint

name = input("Hi! What is your name")

month = randint(1,12)

year = randint(1924,2004)

low_year = 1924

high_year = 2004

guess = 1

for n in range(1,6):

    print("Guess ", n, ": ", name, " were you born in ", month, " / ", year)
    answer = input("yes, earlier, or later?")

    if answer == "yes":
        print("I knew it")
        exit()
    elif answer =="earlier":
        if(n < 5):
            print("Drat! Lemme try again")
        else:
            print("I have other things to do, Good bye.")
            exit()
        high_year = year
        month = randint(1,12)
        year = randint(low_year, high_year)
    elif answer =="later":
        if(n < 5):
            print("Drat! Lemme try again")
        else:
            print("I have other things to do, Good bye.")
            exit()
        low_year = year
        month = randint(1,12)
        year = randint(low_year, high_year)