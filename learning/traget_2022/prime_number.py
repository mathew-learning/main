# Prime Number

def is_prime(input_number):
    status = False
    if input_number > 1:
        for i in range(2, input_number):
            if (input_number % i) == 0:
                status = True
                break
    if status:
        return str(input_number) + "is not a prime"
    else:
        return str(input_number) + " is a prime"


# num = int(input("Enter Number : "))
# print(is_prime(num))


