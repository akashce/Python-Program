def checkstr(str):
    count = 0
    for i in range(len(str)-1):
        count += str[i:i+5] == "Akash"
    return count



str = "Akash is good. Akash knows programming. Akash likes chocolates"
print(checkstr(str))