import json
import random


random.seed()

# with open('streets.json', encoding='utf-8') as file:
#     streets = []
#     for i in file.readlines():
#         if len(i) > 5:
#             streets.append(json.loads(i[2:-2])['street'])
#
# print(streets)
#
#
with open('first_names.json', encoding='utf-8') as file:
    first_names = []
    for i in file.readlines():
        if len(i) > 5:
            first_names.append(json.loads(i[2:-2])['f_name'])

with open('surnames.json', encoding='utf-8') as file:
    surnames = []
    for i in file.readlines():
        if len(i) > 5:
            surnames.append(json.loads(i[2:-2]))
    print(2 if surnames[2]['g'] == first_names[2][2] else 2 - 1)
#
# with open('otchs.json', encoding='utf-8') as file:
#     otchs = []
#     for i in file.readlines():
#         if len(i) > 5:
#             otchs.append(json.loads(i[2:-2])['f_name'])

# n = 89000000000
#
# for i in range(500):
#
#     f_name = random.randint(0, len(first_names) - 1)
#     sur = random.randint(0, len(surnames) - 1)
#     o = random.randint(0, len(otchs) - 1)
#     street = random.randint(0, len(streets) - 1)
#     surname = sur if surnames[sur]['g'] == first_names[f_name]['g'] else sur - 1
#     otch = o if otchs[o]['g'] == first_names[f_name]['g'] else o - 1
#     da.append({'model': 'main.main', 'pk': i + 1, 'fields': {'home': random.randint(1, 10),
#                                                            'corpus': random.randint(1, 2),
#                                                            'apart': random.randint(1, 50),
#                                                            'tel': str(n),
#                                                            'f_name_fk': f_name + 1,
#                                                            'surname_fk': surname + 1,
#                                                            'otch_fk': otch + 1,
#                                                            'street_fk': street + 1}})
#
#     n += 1
#
#
# data += [{'model': 'main.firstnames',
#           'pk': i + 1,
#           'fields': {'f_name': first_names[i]['f_name']}} for i in range(len(first_names))]
# data += [{'model': 'main.surnames',
#           'pk': i + 1,
#           'fields': {'surname': surnames[i]['surname']}} for i in range(len(surnames))]
# data += [{'model': 'main.otchs',
#           'pk': i + 1,
#           'fields': {'otch': otchs[i]['otch']}} for i in range(len(otchs))]
# data += [{'model': 'main.streets',
#           'pk': i + 1,
#           'fields': {'street': streets[i]['sreet']}} for i in range(len(otchs))]
#
# with open('main.json', 'w') as file:
#     json.dump(data, file)
