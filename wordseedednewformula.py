#input
letters = input('say my name: ')

#its for the 2° password
middle = len(letters)

def middle_calculus():
  global middle
  if (middle % 2) == 0:
    middle = int(middle/2) -1
  else:
    middle = int(middle/2)
middle_calculus()
#if you want to see, this is the print that i used to see if it was right
#print(middle)

first_char = letters[0]
lastt_char = letters[middle]
#connect both
both = first_char.upper()+lastt_char

#calculus to transform letters in numbers of something like that
numbers = [ord(letter) - 96 for letter in letters]
numbers = [abs(n) for n in numbers]
strings = [str(integer) for integer in numbers]
strings_filled = [str(item).zfill(2) for item in strings]
a_string = "".join(strings_filled)
numbers = int(a_string)

#last magic
x = numbers * numbers
y = int(x/2)
#1° password
print (f"2V[{y}+{y}]={letters} ")
#2° password
print (f"{y}{both}")
#3° password, i would like to call it the simpliest one
print(numbers)
