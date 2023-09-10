long_str = input("Enter a long string : ")
short_str = input("Enter a short string : ")


sub_strig = False
for i in long_str :
    long_index = long_str.find(i)
    # print(long_str[long_index: long_index+ len(short_str)])
    if i == short_str[0] and long_str[long_index: long_index+ len(short_str)] == short_str :
        sub_strig = True
        break

if sub_strig :
    print("The short string is a sub string of long string")
else :
    print("The short string is not a sub string of long string")