from random import randint

name = input("Hi! What is your name")

month = randint(1,12)

year = randint(1924,2004)

months_name = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",]

low_year = 1924 # update earliest possible year

high_year = 2004 # update latest possible year

guess = 1

for n in range(1,6): #loops five times
    month = randint(1,12)
    year = randint(low_year, high_year) # updates what years to search for based on answer given previously
    print("Guess ", n, ": ", name, " were you born in ", months_name[month-1], " / ", year) #months_name[month-1] takes the name of the month from the months_name list based on the integer month
    #print(month)
    answer = input("yes, earlier, or later?")

    if answer == "yes":
        print("I knew it")
        exit() # exits programs once the correct answer is given
    elif answer =="earlier":
        if(n < 5): # checks if the computer is on the first five guesses
            print("Drat! Lemme try again")
        else: # goes into effect once it goes behind 5 guesses
            print("I have other things to do, Good bye.")
            exit()
        high_year = year
    elif answer =="later":
        if(n < 5):
            print("Drat! Lemme try again")
        else:
            print("I have other things to do, Good bye.")
            exit()
        low_year = year