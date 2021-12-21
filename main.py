# Author: Murtajiz Mehdi
# Date: May 28th, 2021
# Desc: Create program that will print a multiplication table for a number the user inputs (up to 12)


# Display introduction
print('Welcome to my multiplication table program!')

# Prompt for user name
name = input('First, enter your name: ')
print(f'\nHi {name}! Next I am going to ask you for a number and show you all the multiples of that number up to 12.')

# Ask user for number
n = int(input('What number would you like to see the multiples of: '))
print(f"\n{n} is a great number. Below is your {n}'s multiplication table:")
# Program must use a for loop.
for i in range(1, 13):
    print(n, '*', i, '=', n * i)

print(f"\nThank you {name} for using my program. I hope you know your {n}'s now!")

# Program must use a single print statement for each line of asterisks with "*" * a number.
# print(n,'*',i,'=',n*i)
# User can type any number they want not just a 5.
# Number chosen was 4
# You must use variables to store data that is input, and you must first declare and initialize them.
# n = int(input('Enter the number:')), num = input('What number would you like to see the multiples of: ')
#, name = input('First, enter your name: ')