n = (int(input('Введите количество элементов в массиве: ')))
list = [] 
for i in range(n):
    list.append(int(input('Введите целое число: ')))
x = (int(input('Введите число, которое необходимо найти в массиве: ')))
count = 0
for i in range(n):
    if list[i] == x:
        count += 1
print(*list)
print(f'число {x} встречается в массиве {count} раз')