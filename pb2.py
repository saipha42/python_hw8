input_str = input("Enter a text of string : ")

def char_percent( char : chr, text: str) :

    count = 0

    for i in text :
        if i == char :
            count += 1
    
    return count / len(text)

def get_no_repeat(input_str) :
    res = ''
    for i in input_str :
        if i not in res :
            res = res + i
    return res


for char in get_no_repeat(input_str) :

    frequency = char_percent(char, input_str) 
    frequency = '{:>10.2%}'.format(frequency)
    print(char, frequency)