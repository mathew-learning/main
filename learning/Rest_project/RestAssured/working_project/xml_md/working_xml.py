import xml.etree.ElementTree


def min_and_max():
    for value in rule_size_values():
        return "min={} and max={}".format(value[0], value[-1])

tree = xml.etree.ElementTree.parse('RuleCat.xml')
rule_config = tree.getroot()
# for entity in rule_config.findall('Entity'):
#     for prop in entity:
#         if prop.tag == "Fields":
#             for field in prop:
#                 for prop in field:
#                     if prop.tag == "Rules":
#                         for rule in prop:
#                             if rule.text != None and "size" in rule.text.lower():
#                                 size_values = rule.text[5:len(rule)-1].split(',')
#                                 print(min_and_max(size_values))

def rule_size_values(entity_name):
    size_values_list = []
    for entity in rule_config.findall('Entity'):
        if entity.attrib['Name'].lower() == entity_name.lower():
            for prop in entity:
                if prop.tag == "Fields":
                    for field in prop:
                        for prop in field:
                            if prop.tag == "Rules":
                                for rule in prop:
                                    if rule.text is not None and "size" in rule.text.lower():
                                        size_values = rule.text[5:len(rule) - 1].split(',')
                                        size_values_list.append(size_values)

    return size_values_list


print(rule_size_values('NAME_2'))


# def extract_values():
#     for value in rule_size_values():
#         # print("min={} and max={}".format(value[0], value[-1]))
#         yield value
#
#
#
# print(extract_values())

# for car in car_sales.findall('car'):
#     print('\t', car.tag)
#     for prop in car:
#         print('\t\t', prop.tag, end='')
#         if prop.tag == 'price' :
#             print(prop.attrib, end='')
#         print(' =', prop.text)

# new_car = xml.etree.ElementTree.Element('car')
# xml.etree.ElementTree.SubElement(new_car, 'id').text = '4'
# xml.etree.ElementTree.SubElement(new_car, 'brand').text = 'Maserati'
# xml.etree.ElementTree.SubElement(new_car, 'model').text = 'Mexico'
# xml.etree.ElementTree.SubElement(new_car, 'production_year').text = '1970'
# xml.etree.ElementTree.SubElement(new_car, 'price', {'currency': 'EUR'}).text = '61800'
# car_sales.append(new_car)
# tree.write('newcars.xml', method='')