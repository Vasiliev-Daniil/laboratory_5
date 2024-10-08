from random import randint, choice

n = randint(4, 30)
print("Перед вами куча, с количеством камней равным " + str(n))
computer_move = choice([True, False])
while n > 1:
    if computer_move:
        if n > 3:
            move = randint(1, 3)
        else:
            move = randint(1, n)
        n -= move
        print("ХОД ПРОТИВНИКА. Противник взял камней: " + str(move) + ". В куче осталось: " + str(n) + ".\n")
    else:
        print("ВАШ ХОД.")
        if n > 2:
            top = 3
        else:
            top = n
        move = input("Введите количество камней (от 1 до " + str(top) + "): ")
        while True:
            try:
                move = int(move)
                if 1 <= move <= top:
                    break
                else:
                    move = input("Были введены некорректные значения. Введите количество камней (от 1 до " + str(top)
                                 + "): ")
            except ValueError:
                move = input(
                    "Были введены некорректные значения. Введите количество камней (от 1 до " + str(top) + "): ")
        n -= move
        print("В куче осталось: " + str(n))
    computer_move = not computer_move

if n == 0:
    if not computer_move:
        print("\nВы выйграли!")
    else:
        print("\nВы проиграли (")
else:
    if computer_move:
        print("\nВы выйграли!")
    else:
        print("\nВы проиграли (")
