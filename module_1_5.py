immutable_var = 1,2,3,'кит',True
print(immutable_var)
mutable_list = [1,2,3,'кит',True]
mutable_list[3] = 'кот'
print(mutable_list)
mutable_list.append('кашалот и петунья')
print(mutable_list)
mutable_list.remove('кашалот и петунья')
mutable_list.extend(['До свидания','и','спасибо','за','рыбу','!'])
print(mutable_list)
