from collections import OrderedDict
from pprint import pprint
import csv
import re


def remove_duplicates(list_: list):
    list_ = list(csv.reader(list_, delimiter=','))
    for list1 in list_:
        k = list_.index(list1)
        while k < len(list_) - 1:
            k += 1
            zip_list = list(zip(list1, list_[k]))
            if zip_list[0][0] == zip_list[0][1] and zip_list[1][0] == zip_list[1][1]:
                new_list = list(OrderedDict.fromkeys(list1 + list_[k]))
                index = list_.index(list1)
                list_.remove(list_[k])
                list_.remove(list1)
                list_.insert(index, new_list)

    return list_


with open("phonebook_raw.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    # pprint(contacts_list)

teleph_num = '(\+7|8)\s*\(*(\d*|\d{3})\)*(-|\s*)(\d{3})(\-?|\s)(\d{2})(\-?|\s)(\d{2})'
add_num = '\(*(доб)(.?)\s*(\w*)\)*'
fio = '([А-ЯЁ][а-яё]*)(\s|,)([А-ЯЁ][а-яё]*)(\s)([А-ЯЁ][а-яё]*),{2,3}'
fi = '^([А-ЯЁ][а-яё]*)\s([А-ЯЁ][а-яё]*),{3}'

p_num = re.compile(teleph_num)
p_add_num = re.compile(add_num)
p_fio = re.compile(fio)
p_fi = re.compile(fi)

my_list = []

for list_ in contacts_list:
    list_ = ','.join(list_)
    list_ = p_num.sub(r'+7(\2)\4-\6-\8', list_)
    list_ = p_fio.sub(r'\1,\3,\5,', list_)
    list_ = p_add_num.sub(r'\1.\3', list_)
    list_ = p_fi.sub(r'\1,\2,,', list_)
    my_list.append(list_)

with open("phonebook.csv", "wt", encoding='utf-8', newline='') as f:
    datawriter = csv.writer(f, delimiter=",")
    for string in [','.join(string) for string in remove_duplicates(my_list)]:
        datawriter.writerow(string.split(','))
