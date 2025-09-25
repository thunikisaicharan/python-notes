# simple login system
username = "admin"
password = "1234"

input_username = input("enter username:")
input_password = input("enter password:")

if(input_username == username) & (input_password == password):
    print("access granted")
else:
    print("access denied ")