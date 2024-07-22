my_dict = {'Alex' : 1987, 'Anton' : 1999, 'Maksim' : 2001}
print(my_dict)
print(my_dict['Maksim'])
my_dict['Pavel'] = 2000
print(my_dict['Pavel'])
my_dict.update({'Danil' : 1997, 'Roma' : 1998})
del my_dict['Alex']
print(my_dict)
my_set = {1, 2, 2, 2, 3, 4, 'привет', 'пока', 'пока'}
print(my_set)
my_set.add('Hello')
my_set.add(5)
my_set.discard(4)
print(my_set)
