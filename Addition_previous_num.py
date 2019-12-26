#Addition of current number and previous number
def sum_plus_previous_num_sum(num):
    previous_num = 0
    for i in range(num):
        sum = i + previous_num
        print(sum)
        previous_num = i


sum_plus_previous_num_sum(10)
