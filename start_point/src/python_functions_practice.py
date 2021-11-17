def return_10():
    return 10 

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def length_of_string(string):
    return len(string)

def join_string(string1, string2):
    return string1 + string2

def add_string_as_number(string1, string2):
    return int(string1) + int(string2)

def number_to_full_month_name(num_month):
    list_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return list_months[num_month-1]

def number_to_short_month_name(num_month):
    return (number_to_full_month_name(num_month))[0:3]

def volume_of_cube(num_length):
    return (num_length**3)

def reversed_string(reverse_string):
    return reverse_string[::-1]

def fahrenheit(celcius_test):
    return (celcius_test - 30)/2
    
