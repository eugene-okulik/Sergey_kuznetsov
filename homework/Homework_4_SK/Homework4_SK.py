my_dict = {'tuple': 'value', 'list': 'value2', 'dict': 'value3', 'set': 'value4'}
# my_dict = dict(tuple='value', list='value2', dict='value3', set='value4')


my_dict['tuple'] = (1, 5, None, 'text', 3.11)
my_dict['list'] = [8, True, 1, 1, 3.675]
my_dict['set'] = {1, 45, 8, True, 1, 1, 3.675, None, 'cat'}
my_dict['dict'] = {1: 2, 'milk': 'shop', 232: 12, 'ddd': 1, 121: 'mnc'}

print((my_dict['tuple'])[-1])

my_dict['list'].append(13)
my_dict['list'].pop(1)
print(my_dict['list'])

(my_dict['dict'])['i am a tuple'] = 'added'
my_dict['dict'].pop('milk')
print(my_dict['dict'])

my_dict['set'].add(10)
my_dict['set'].remove(45)
print(my_dict['set'])

print(my_dict)
