import yaml

# to read yaml file data.
with open('sample.yaml', 'r') as f:
    yaml_data = yaml.safe_load(f)
    f.close()
print(yaml_data)
# to create python file
python_file = open('sample.py', 'w')

def size_values(data):
    print(data)
size_values(yaml_data)




#
# def convert_to_variable_value(dic_value):
#     if dic_value is None:
#         value = '""\n'
#         return value
#     elif type(dic_value) is list:
#         value = "{yaml_value}\n".format(yaml_value=dic_value)
#         return value
#     else:
#         value = '"{yaml_value}"\n'.format(yaml_value=dic_value)
#         return value
#
#
# def convert_to_python_file(data):
#     for key in data:
#         if type(data[key]) is dict:
#             nested_dic = data[key]
#             python_file.writelines("#{key}\n".format(key=key))
#             for nest_key in nested_dic:
#                 value = convert_to_variable_value(nested_dic[nest_key])
#                 python_file.writelines(nest_key + " = " + value)
#         else:
#             value = convert_to_variable_value(data[key])
#             python_file.writelines(key + " = " + value)
#     python_file.close()
#     return


#
#
# def convert_to_python_file(data):
#     for key in data:
#         if type(data[key]) is dict:
#             nested_dic = data[key]
#             python_file.writelines("#{key}\n".format(key=key))
#             for nest_key in nested_dic:
#                 if nested_dic[nest_key] is None:
#                     value = "''\n"
#                     python_file.writelines(nest_key + " = " + value)
#                 elif type(nested_dic[nest_key]) is list:
#                     value = "{yaml_value}\n".format(yaml_value=nested_dic[nest_key])
#                     python_file.writelines(nest_key + " = " + value)
#                 else:
#                     value = "'{yaml_value}'\n".format(yaml_value=nested_dic[nest_key])
#                     python_file.writelines(nest_key + " = " + value)
#         elif type(data[key]) is list:
#             value = "{yaml_value}\n".format(yaml_value=data[key])
#             python_file.writelines(key + " = " + value)
#         elif data[key] is None:
#             value = "''\n"
#             python_file.writelines(key + " = " + value)
#         else:
#             value = "'{yaml_value}'\n".format(yaml_value=data[key])
#             python_file.writelines(key + " = " + value)
#     python_file.close()
#     return


# def main():
#     convert_to_python_file(yaml_data)
#
#
# main()
