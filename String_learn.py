# Accept string from user and disply the char at even index
def printevenstr(str):
    for i in range(0,len(str),2):
        print("index[",i,"]",str[i])

inputstr = input("Enter the string")

print("Original string is: ",inputstr)

print("Printitng only even index")

printevenstr(inputstr)