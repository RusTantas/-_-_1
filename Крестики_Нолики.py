
def chek_winner():                                                     # проверка победителя, очень долгая можно лучше, надо подумать
    if area[0][0] == "X" and area[0][1] == "X" and area[0][2] == "X":
        return "X"
    if area[1][0] == "X" and area[1][1] == "X" and area[1][2] == "X":
        return "X"
    if area[2][0] == "X" and area[2][1] == "X" and area[2][2] == "X":
        return "X"
    if area[0][0] == "X" and area[1][0] == "X" and area[2][0] == "X":
        return "X"
    if area[0][1] == "X" and area[1][1] == "X" and area[2][1] == "X":
        return "X"
    if area[0][2] == "X" and area[1][2] == "X" and area[2][2] == "X":
        return "X"
    if area[0][0] == "X" and area[1][1] == "X" and area[2][2] == "X":
        return "X"
    if area[0][2] == "X" and area[1][1] == "X" and area[2][0] == "X":
        return "X"
    if area[0][0] == "0" and area[0][1] == "0" and area[0][2] == "0":
        return "0"
    if area[1][0] == "0" and area[1][1] == "0" and area[1][2] == "0":
        return "0"
    if area[2][0] == "0" and area[2][1] == "0" and area[2][2] == "0":
        return "0"
    if area[0][0] == "0" and area[1][0] == "0" and area[2][0] == "0":
        return "0"
    if area[0][1] == "0" and area[1][1] == "0" and area[2][1] == "0":
        return "0"
    if area[0][2] == "0" and area[1][2] == "0" and area[2][2] == "0":
        return "0"
    if area[0][0] == "0" and area[1][1] == "0" and area[2][2] == "0":
        return "0"
    if area[0][2] == "0" and area[1][1] == "0" and area[2][0] == "0":
        return "0"
    return "*"


def draw_area():                      # делаем так что бы линия превратилась в поле для игры
    for i in area:
        print(*i)
    print()

area = [["*", "*" ,"*" ], ["*", "*" ,"*" ], ["*", "*" ,"*" ]]
print("Добро пожалавать в крестики нолики")
print("------------------------------------------------")

for turn in range(1, 10):                                  # считаем ходы
    print(f'Ход:{turn}')                                   # считаем ходы будет работать только так, без f не будет показаывать какой ход. возвращает в фигурных скаобках значение turn
    if turn % 2 == 0:                                     # все нечетные ходы это крестики все четные нолики
        turn_char = "0"
        print("Ходят нолики")
    else:
        turn_char = "X"
        print("Ходят крестики")
    row = int(input("Введите номер строки (1, 2, 3)"))-1
    colum = int(input("Введите номер строки (1, 2, 3)"))-1
    if area[row][colum] == "*":                            # проверка занятности ячейки, если уже занята то пропускает ход
        area[row][colum] = turn_char
    else:
        print("Ячейка уже занята, вы пропускаете ход")
        draw_area()
        continue

    draw_area()

    if chek_winner() == "X":
        print("Победили крестики")
        break
    if chek_winner() == "0":
        print("Победили нолики")
        break





