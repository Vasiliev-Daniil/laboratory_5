from math import sqrt


# Получение данных от пользователя и проверка их корректности
def get_value(name):
    res = input("Введите значение координаты " + name + ": ")
    while not res.isdigit():
        res = input("Были введены некорректные данные. Введите значение координаты " + name + ": ")
    return int(res)


x = get_value("x")
y = get_value("y")
z = get_value("z")
print("Длина вектора: " + str(sqrt(x ** 2 + y ** 2 + z ** 2)))
