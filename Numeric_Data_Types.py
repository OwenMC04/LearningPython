num = 2
# print(num + ' is the number') # Won't work as it thinks you are trying to add an int to a string
print(str(num) + ' is the number') # Changed the int to a string and will work fine
first_num = input('Enter a number: ')
second_num = input('Enter a second number: ')
print(first_num + second_num) # as the input function always uses strings it will concatenate rather than add
print(int(first_num) + int(second_num)) #convert to int and add *Only works if input is an int
print(float(first_num) + float(second_num)) #convert to float and add
