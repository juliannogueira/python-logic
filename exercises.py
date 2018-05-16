#Logic 

#Conditional statements gives us the ability to check conditions and make decisions based on the condition.

#In this assignment, you'll be asked to create conditional statements using if, elif and else. 

# Please commit and push your code after each completed exercise.

#1. Declare a variable named weather and assign it a string value of 'rain'. Next create a conditional statement that will check the weather and print 'Bring an umbrella' if weather equals 'rain'.

weather = 'rain'

if weather == 'rain':
    print('Bring an umbrella')

#2 Declare a variable named score and assign it a number value of 70. Next create a conditional statement that will check the score and print 'You pass!' if the score is 70 and above and print 'Study harder!' if the score is less than 70.

score = 70
if score >= 70:
    print('You pass!')
elif score < 70:
    print('Study harder!')

#3. Declare a variable named download_speed and assign it a data value of 50. Next create a conditional statement that will check the download speed and print the following based on the condition:

download_speed = 50
if download_speed <= 50:
    print('Basic Package')
elif download_speed <= 100:
    print('Premium Package')
else:
    print('Platinum Package')

# <= 50: 'Basic Package'
# <=100: 'Premium Package'
# >100: 'Platinum Package'

 #4 Function - check_password
 #Create a function named check_password which takes a parameter password.

def check_password(password):
    if password == 'qwerty':
        return True

password_result = check_password('qwerty')
print(password_result)

 #The function will return true if the password passed into the function is equal to 'qwerty'. Declare a variable named password_result and print your result.

#5 Function check_login
#Create a function named check_login which takes a parameter login.

def check_login(login):
    if login == 'DevLeague':
        print('Login Success')
    else:
        print('Re-enter')

check_login('DevLeague')

#The function will print 'Login Success' if the login passed into the function is equal to 'DevLeague' and print 'Re-enter Login' if it doesn't.

#6 Function malware_type
#Create a function named malware_type which takes a parameter malware. 

def malware_type(malware):
    if malware == 'adware':
        print('Low Threat')
    elif malware == 'virus':
        print('Do no share files')
    else:
        print('I hope you backed up your data')

type_of = 'virus'
malware_type(type_of)

#The function will print the following based on the following conditions:
#if malware is adware: 'Low Threat'
#if malware is virus: 'Do not share files'
#default message 'I hope you backed up your data'

#7 Function encryption
#Create a function named encryption which takes a parameter keys.

def encryption(keys):
    if len(keys) == 5:
        print('Encryption Success')
    else:
        print('Encryption Fail')

some_key = 'qwerty'
some_other_key = 'qwert'

encryption(some_key)
encryption(some_other_key)

#The function will print 'Encryption Success' if the keys passed into function has 5 characters and print 'Encryption Fail' if it doesn't.

#8 Function even_cryptography
#Create a function named even_cryptography which takes a parameter num.

def even_cryptography(num):
    try:
        if num % 2 == 0:
            print('Decryption Success')
        elif num % 2 == 1:  
            print('Decryption Fail')
        else:
            print('Decryption Super Fail')
    except:
        print('Decryption Super Fail')

even_cryptography(17)
even_cryptography(8)
even_cryptography(17.5)
even_cryptography('cat')

#The function will print 'Decryption Success' if the number passed into the function is even and print 'Decryption Fail' if it isn't.

#9 Function bandwidth
#Declare a variable named mbps and assign it a list of 5 number values of your choosing. 

mbps = [1, 2, 10, 20, 2018]

def bandwith(usage):
    add_all = sum(usage)
    if add_all <= 50:
        print('Light User')
    elif add_all <= 100:
        print('Moderate User')
    elif add_all <= 150:
        print('Multi Media User')
    else:
        print('Power User!')

bandwith(mbps)

#Next, create a function named bandwidth which takes a parameter usage.
#The function will sum up the list of numbers and print the following messages based on the condition:

#if sum <= 50: 'Light User'
#if sum <= 100: 'Moderate User'
#if sum <=150: 'Multi Media User'
#if sum >150: 'Power User'

#10 Function ssh_keys
#Create a function named ssh_keys which takes two parameters public and private.

def ssh_keys(public, private):
    if public != private:
        return False

ssh_connection = ssh_keys(1234, 4321)
print(ssh_connection)

#The function will return false if public and private aren't equal and return true if they are equal.

#Declare a variable named ssh_connection and print your result.

#11 Function largest_num
#Create a function named largest_num which takes three parameters: num_1, num_2 and num_3.

def largest_num(num_1, num_2, num_3):
    num_list = [num_1, num_2, num_3]
    return max(num_list)
    
large_num_result = largest_num(100, 1000, 1000000)
print(large_num_result)

#The function will find the largest number among any three numbers that are passed into the function. Declare a variable named large_num_result and print your results.

#12 Function pos_neg
#Create a function named pos_neg which takes a parameter num.

def pos_neg(num):
    if num > 0:
        print('Positive Number')
    elif num == 0:
        print('Zero')
    else:
        print('Negative Number')

some_num = -98
pos_neg(some_num)

#The function will print 'Positive Number' if the number passed in is positive, print 'Zero' if the number is 0 and print 'Negative Number' for a negative number.

#13 Function name_caps
#Create a function named name_caps which takes a parameter name.

def name_caps(name):
    name_len = len(name)
    if name_len <= 5:
        name = name.title()
    elif name_len <= 10:
        name = name.upper()
    else:
        name = name
    print(name)

my_name = 'julian'

name_caps(my_name)

#The function will check the number of characters in the name that is passed into the function and do the following:

#if characters in name <=5: capitalize the first letter in the name
#if characters in name <=10: captialize all the letters in the name
#if characters in name >10: leave the letters as is

#Print your results

#14 Function leap_year

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        print('The year ' + str(year) + ' is a leap year.')
    else:
        print('They year ' + str(year) + ' is not a leap year.')

leap_year(1996)
leap_year(2000)
leap_year(2016)
leap_year(2018)

#A leap year occurs every four years. Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but are leap years if they are exactly divisible by 400.

#Create a function named leap_year which takes a parameter year.
#The function will print 'The year x is a leap year.' where x is the year value that is passed into the function and print 'The year x is not a leap year.' if it isn't a leap year.


