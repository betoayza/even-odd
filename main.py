number = 0

while(number != -1):
    number = int(input("Hey, welcome to Even-Odd!\nPlease, enter a number behind 1-1000 [-1 to exit]: "))
        
    print("You are entered: ", number)

    if number >= 1 and number <= 1000:
        if(number % 2 == 0):
            print(number," is even")
        else:
            print(number, " is odd")
    else:
        print("Invalid number :/")

print("Thanks, come back later!")