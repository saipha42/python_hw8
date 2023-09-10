first_name = input("Enter user first name : ")
last_name = input("Enter last name : ")
gender = input("Enter gender (m/f) : ")

user_name = (gender + last_name[0] + first_name[0:6]).upper()
print('user name : ', user_name)