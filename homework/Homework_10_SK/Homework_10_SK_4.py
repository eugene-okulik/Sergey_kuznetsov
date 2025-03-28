PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_new = PRICE_LIST.strip().split('\n')

new_dict = {item.rsplit(' ', 1)[0]: int(item.rsplit(' ', 1)[1][:-1]) for item in price_new}

print(new_dict)
