# Python Program to calculate Sum of Series 1²+2²+3²+….+n²
 
number = int(input("Please Enter any Positive Number  : "))
total = 0

total = (number * (number + 1) * (2 * number + 1)) / 6

print("The Sum of Series upto {0}  = {1}".format(number, total))