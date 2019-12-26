def reversecheck(num):
    originalnum = num
    reversenum = 0
    while(num > 0):
        reminder = num % 10
        reversenum = (reversenum * 10) + reminder
        num = num // 10
    if (originalnum == reversenum):
        return True
    else:
        return False


print((reversecheck(121)))
