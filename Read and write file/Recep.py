def get_shop_list_by_dishes(dishes, person):
    qual = {}
    for name_ in dishes:
        for key_, value_ in cook_book.items():
            if name_ == key_:
                for x in value_:
                    if dishes.count(name_) > 1:
                        qual[x['ingredient_name']] = {'measure': x['measure'], 'quantity': (x['quantity'] *
                                                                                            dishes.count(
                                                                                                name_) * person)}
                    else:
                        qual[x['ingredient_name']] = {'measure': x['measure'], 'quantity': (x['quantity'] * person)}
    return qual


cook_book = {}

with open('recept.txt', encoding='utf8') as recep:
    while True:
        name = recep.readline().strip()
        if name == '':
            break
        cook_book[name] = []
        qua_ingr = int(recep.readline().strip())
        while qua_ingr > 0:
            qua_ingr -= 1
            ingr_ = recep.readline().strip().split(' | ')
            ingr = {'ingredient_name': ingr_[0], 'quantity': int(ingr_[1]), 'measure': ingr_[2]}
            cook_book[name] += [ingr]
        recep.readline()

x = ['Омлет', 'Омлет']
print(get_shop_list_by_dishes(x, 2))
