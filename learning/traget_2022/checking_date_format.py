

def check_format(input_datetime):
    input_date = input_datetime.split(" ")[0]
    status = False
    i = 0
    while i < len(input_date.split('-')):
        if input_date.split('-')[i] in [str(value) for value in range(1, 2022)]:
            if input_date.split('-')[i+1] in [str(value) if value >= 10 else "0"+str(value) for value in range(1, 13)]:
                if input_date.split('-')[i+2] in [str(value) if value >= 10 else "0"+str(value) for value in range(1, 32)]:
                    status = True
        i+=len(input_date.split('-'))
    return status


print(check_format("2019-12-03 23:00:35"))