import requests
import json

class InvalidInputError:
    pass


def print_menu():
    pass
# prints user menu - nothing else happens here;

def read_user_choice():
    pass
# reads user choice and checks if it's valid;
# returns '0', '1', '2', '3' or '4'

def name_is_valid(name):
    if name == "":
        return False
    else:
        return True
# checks if name (brand or model) is valid;
# valid name is non-empty string containing
# digits, letters and spaces;
# returns True or False;

def enter_id():
    try:
        id = input("Enter id: ")
        if id == "":
            return
        elif not id.isdigit():
            raise TypeError
    except TypeError:
        print("Id should be Integer")
    else:
         return id


def enter_production_year():
    try:
        year = input("Enter id: ")
        if year == "":
            return
        elif not year.isdigit():
            raise TypeError
        elif year not in range(1900, 2001):
            raise InvalidInputError
    except TypeError:
        print("Id should be Integer")
    except InvalidYearError:
        print()
    else:
         return year



def enter_name(what=None):
    try:
        car_name = input("Enter name : ")
        if not name_is_valid():
            raise InvalidInputError
    except InvalidInputError:
        print("Entered name is not valid")
    else:
        return car_name
# allows user to enter car's name (brand or model) and checks if it's valid;
# uses name_is_valid() to check the entered name;
# returns string or None  (if user enters an empty line);
# argument describes which of two names is entered currently ('brand' or 'model');


def check_server(cid=None):
    # returns True or False;
    # when invoked without arguments simply checks if server responds;
    # invoked with car ID checks if the ID is present in the database;
    request = requests.get("http://localhost:3000")
    if cid is None and request.status_code == requests.codes.ok:
        return request.reason
    elif cid is not None:
        request = requests.get("http://localhost:3000/cars")
        data = json.loads(request.text)
        if cid in data:
            return True
    else:
        return False

def add_car():
    car_id = 1
    car_company = 'Ford'
    car_model = 'figo'
    car_MFT = '2021'
    new_car = {
        "Company":car_company,
        "Model":car_model,
        "MFT":car_MFT
    }
    data = json.dumps(new_car)
    print(data)
    h_content = {'Content-Type': 'application/json'}
    request = requests.post("http://localhost:3000/cars", headers=h_content, data=data)
    return request.status_code, request.reason

def delete_car():
    request = requests.delete("http://localhost:3000/cars/32")
    print(request.status_code, request.reason)

def update_car():
    car_company = 'VW'
    car_model = 'polo'
    car_MFT = '2021'
    new_car = {
        "Company": car_company,
        "Model": car_model,
        "MFT": car_MFT
    }
    data = json.dumps(new_car)
    h_content = {'Content-Type': 'application/json'}
    request = requests.put('http://localhost:3000/cars/1', headers=h_content, data=data)
    print(request.status_code, request.reason)


def list_cars():
    request = requests.get("http://localhost:3000/cars")
    print(request.text)

def print_header():
    request = requests.get("http://localhost:3000/cars")
    data =  request.text
    table_headers = json.loads(data)[0].keys()
    for key in table_headers:
        print(key, end=",")
    print()

def print_car():
    print_header()
    request = requests.get("http://localhost:3000/cars")
    data = json.loads(request.text)[0]
    table_headers = data.keys()
    for i in range(len(table_headers)):
        data = json.loads(request.text)[i]
        for key in table_headers:
            print(data[key], end=",")
        print()

# print(check_server(cid=1))
print(add_car())
update_car()
# # list_cars()
# print_car()

# delete_car()
    # print_menu()
    # choice = read_user_choice()
    # if choice == '0':
    #     print("Bye!")
    #     exit(0)
    # elif choice == '1':
    #     list_cars()
    # elif choice == '2':
    #     add_car()
    # elif choice == '3':
    #     delete_car()
    # elif choice == '4':
    #     update_car()
