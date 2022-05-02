
class FileNotFound(Exception):
    pass


l = ["hello.err", "hello.err"]
# try:
#     for file_name in l:
#         if ".csv" in file_name:
#             print(True)
#         else:
#             raise FileNotFound
# except FileNotFound:
#     print(".csv file Not Found")

for file_name in l:
    if ".csv" in file_name:
        print(True)
        break
else:
    print("File Not Found")