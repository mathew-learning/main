# Amstrong number

def is_amstrong_number(num):
    sum = 0
    for i in str(num):
        sum = sum + int(i)**len(str(num))
    if sum == num:
        return "is as Amstrong Number"
    else:
        return "Not an Amstrong Number"

print(is_amstrong_number(1634))