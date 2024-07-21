immutable_var = (1, 2, 'a', 'b', True)
print(immutable_var)
immutable_var.extend ("c") # кортеж является не изменяемымы объектом а используется он как хранилище
mutable_list = [1, 2, 'a', 'b']
mutable_list.extend([True])
print(mutable_list)
