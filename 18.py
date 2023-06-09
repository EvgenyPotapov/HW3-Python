n = int(input("Введите количество элементов в массиве: "))
arr = []
for i in range(n):
    element = int(input("Введите целое число: "))
    arr.append(element)

x = int(input("Введите число X: "))

closest = arr[0]  # Инициализация переменной ближайшего элемента первым элементом массива
diff = abs(x - arr[0])  # Инициализация переменной разницы минимальной разницей

# Поиск ближайшего элемента
for i in range(1, n):
    if abs(x - arr[i]) < diff:
        closest = arr[i]
        diff = abs(x - arr[i])

print(f"Ближайший к числу {x} элемент в массиве: {closest}")
