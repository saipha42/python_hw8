integer = int(input("Enter an integer : "))

def int_to_binary(integer) :

    if integer ==0 :
        print("The input integer is 0. No Conversion.")
        return None
    if integer < 0 :
        print("The input integer is negative. No Conversion.")
        return None
    
        
    binary = ''
    while integer > 0 :

        rem = integer % 2
        binary = str(rem) + binary

        integer = integer // 2
    return binary


def binary_to_int (binary) :

    if binary == None :
        return
    binary = binary[::-1]
    integer = 0
    for i in range(0, len(binary)) :
        res = int(binary[i]) * (2**(int(i)))
        integer += res
    return integer

binary = int_to_binary(integer)
integer = binary_to_int(binary)

if binary != None  :
    print("Binary of integer ", integer , "is :",binary)

if integer != None :
    print( "Integer of binary ", binary, " is :",integer)