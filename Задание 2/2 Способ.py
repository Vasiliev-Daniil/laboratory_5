x = input("Введите значение первой переменной: ")

while not x.isdigit():
    x = input("Были введены некорректные данные. Введите значение первой переменной: ")
x = int(x)

y = input("Введите значение второй переменной: ")

while not y.isdigit():
    y = input("Были введены некорректные данные. Введите значение второй переменной: ")
y = int(y)

y = x + y
x = y - x
y = y - x
print("X: " + str(x) + "\nY: " + str(y))