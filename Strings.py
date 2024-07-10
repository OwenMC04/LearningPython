first_name = input('What is your first name: ') # Ask user for input
first_name = first_name.capitalize() #Capitalises first letter of first word
print(first_name) 
first_name= first_name.upper() #Capitalises whole string
print(first_name)
first_name = first_name.lower() #Makes whole string loweracse
print(first_name)
print('Hello ' + first_name.capitalize())

#String Formatting

last_name = input('What is your last name: ')
first_name = first_name.capitalize()
output = 'Hello, ' + first_name + ' ' + last_name #How I normally do it
print(output)
output = 'Hello,  {}{}'.format(first_name, last_name) #Formats accoring to order of variables
print(output)
output = 'Hello, {0}{1}'.format(first_name, last_name) #Formats accoring to my order i.e. first_name = 0
print(output)
output = 'Hello, {1}{0}'.format(first_name,last_name)
print(output)
output = f'Hello, {first_name} {last_name}' #Best way as self documenting only avalible in Python 3
print(output)