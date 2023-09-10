
digits = input("Enter the first 9 digits of an ISBN-10 as a strig : ")

summation = 0
for i in range(len(digits)) :
    index = i + 1
    summation += index * int(digits[i])

last_digit = summation % 11
if last_digit == 10 :
    last_digit = 'X'

print( "Your ISBN-10 number is ",digits+ str(last_digit))
