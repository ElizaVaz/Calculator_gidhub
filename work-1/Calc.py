print("Привет!")
print("")


def my_vozmognoste():
    print("0.                Мои возможности)      ")
    print("1. сложение  ----------------------------->   +")
    print("2. вычитание  ---------------------------->   -")
    print("3. умножение  ---------------------------->   *")
    print("4. деление  ----------------------------->    /")
    print("5. целочисленное деление  -------------->     //")
    print("6. взятие остатка  ---------------------->    %")
    print("7. возведение в степень  --------------->     **")
    print("8. квадратный корень числа  ------------->    8 (√)")
    print("9. перевод в десятичную cист.  ----------->   9")
    print("")


def a_esli():
    print("")
    print("Если хотите воспользоваться калькулятором - нажмите Enter или введите 'да'.")
    print("Так же, вы может произвести АНАЛИЗ числа (введя 'анализ').")
    print("               Возможности калькулятора будут всегда перед вами).")
    return input()


otvet = a_esli()


def is_it_num(p_num):
    if not p_num.isdigit() or p_num == "":
        print("Хах, сработала защита от дураков)")
        return False
    else:
        return True


def get_num_only(p_ch):
    v_ch = p_ch
    while not is_it_num(v_ch):
        v_ch = input("Введите только int: ")
    return v_ch


def is_it_num_or_float(p_num):
    if p_num.isdigit():
        return True
    elif p_num == "":
        print("Хах, сработала защита от дураков)")
        return False
    x = ""
    for i in str(p_num):
        if i not in ".,":
            x += i
    if x.isdigit() or x[0] == "-" and x[1:].isdigit():
        return True
    print("Сори, но только int или float")
    print("Давайте всё таки введём число.")
    return False


def get_num_or_float(p_ch):
    v_ch = p_ch
    while not is_it_num_or_float(v_ch):
        v_ch = input("Введите int или float: ")
    return v_ch


def what_is_there(p_num):  # p_num - текст
    print("В числе", p_num, "количества разрядов равно", len(str(p_num)))

    # Блок определения колличества каждой из цифр:
    symbols = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Количество в этом числе разных цифр до начала подсчёта
    #         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    int_num = int(p_num)
    num = int_num
    for i in range(0, len(str(int_num))):
        current_num = num % 10
        symbols[current_num] += 1
        num = num // 10

    for i in range(0, 10):
        if symbols[i] != 0:
            print("Число", i, "встречалось", symbols[i], "раз в числе", p_num)

    # Блок чётное или не чётное:
    if int_num % 2 == 0:
        print("Число", p_num, "- чётное")
    else:
        print("Число", p_num, "- Нечётное")
    # Блок суммы цифр числа:
    symm = 0
    num = int_num
    for i in range(0, len(p_num)):
        symm += num % 10
        num = num // 10
    print("Сумма цифр -", symm)


# Блок является ли число простым, если не простое, то выведу все делители числа:
def easy_num(p_num):  # p_num - текст...
    int_num = int(p_num)
    c = 0
    x = 2
    while c != 1 and x < int_num:
        if (int_num / x) % 1 == 0:
            c = 1
        else:
            x += 1
    if c == 1:
        delit_num(p_num)
    else:
        print("Число", p_num, "- простое")


def delit_num(p_num):
    if len(p_num) > 4:
        print("СЛИШКОМ МНОГО ВОЗМОЖНЫХ ДЕЛИТЕЛЕЙ!")
    int_num = int(p_num)
    x = 2
    vs_x = ""
    while x < int_num:
        if (int_num / x) % 1 == 0:
            if vs_x == "":
                vs_x = str(x)
            else:
                vs_x += ", " + str(x)
        x += 1

    print("Число", p_num, "нацело делится на", vs_x)


# Блок проверяющий является ли число квадратратом или кубом целового число:
def kvadr_kyb_num(p_num):
    p_num = int(p_num)
    if p_num ** 0.5 % 1 == 0:
        print("Число", p_num, "является квадратом числа", int(p_num ** 0.5))
    if p_num ** (1 / 3) % 1 == 0:
        print("Число", p_num, "является кубом числа", int(p_num ** (1 / 3)))


def is_norm_number(p_ch1, p_ch2):
    try:
        print("*****")
        print(ch1, "в", str(ch2) + "-ной сист. исчисления  =  ", int(str(p_ch1), int(p_ch2)), "в 10-ой сист. исчисления")
        print("*****")
    except ValueError:
        print("Извините, мы переводим только целые числа и числа которые можно перевести.")



def koren(ch1):
    if float(ch1) >= 0:
        ch1 = float(ch1)
        if ch1 % 1 == 0:
            ch1 = int(ch1)
        s = ch1 ** 0.5
        if s % 1 == 0:
            s = int(s)
        print("√" + str(ch1), "=", s)
    else:
        print("Нет корней, т.к. ОНО ОТРИЦАТЕЛЬНОЕ")


while "да" in otvet or "y" in otvet or otvet == "" or "ана" in otvet or "АНА" in otvet or "Ана" in otvet \
        or otvet == "" or "0" in otvet:

    if "Ана" in otvet or "ана" in otvet or "АНА" in otvet:
        print("")
        num_to_check = input("Введите число для анализа: ")
        num_to_check = get_num_only(num_to_check)

        what_is_there(num_to_check)
        easy_num(num_to_check)
        kvadr_kyb_num(num_to_check)

    else:
        my_vozmognoste()
        ch1 = input("Введите число: ")
        ch1 = get_num_or_float(ch1)
        symbol = input("Введите число под которым стоит знак (действие): ")
        if "9" in symbol:
            ch2 = input("Из какой сист. исчесления вы ходите перевести число: ")
            ch2 = get_num_only(ch2)
            is_norm_number(ch1, ch2)
        elif "√" in symbol or "корен" in symbol or "Корен" in symbol or "8" in symbol:
            koren(ch1)
        else:
            ch1 = float(ch1)
            ch2 = input("Введите второе число: ")
            ch2 = get_num_or_float(ch2)
            ch2 = float(ch2)

            if ch1 % 1 == 0:
                ch1 = int(ch1)
            if ch2 % 1 == 0:
                ch2 = int(ch2)

            if "+" in symbol or "1" in symbol:
                kon = ch1 + ch2
                if kon % 1 == 0:
                    kon = int(kon)
                print(ch1, "+", ch2, "=", kon)
            elif "-" in symbol or "2" in symbol:
                kon = ch1 - ch2
                if kon % 1 == 0:
                    kon = int(kon)
                print(ch1, "-", ch2, "=", kon)
            elif "**" in symbol or "7" in symbol:
                kon = ch1 ** ch2
                if kon % 1 == 0:
                    kon = int(kon)
                print(ch1, "**", ch2, "=", kon)
            elif "*" in symbol or "3" in symbol:
                kon = ch1 * ch2
                if kon % 1 == 0:
                    kon = int(kon)
                print(ch1, "*", ch2, "=", kon)
            elif "//" in symbol or "5" in symbol:
                if ch2 != 0:
                    kon = ch1 // ch2
                    if kon % 1 == 0:
                        kon = int(kon)
                    print(ch1, "//", ch2, "=", kon)
                else:
                    print("На ноль делить НИЗЯЯЯЯ!")
            elif "/" in symbol or "4" in symbol:
                if ch2 != 0:
                    kon = ch1 / ch2
                    if kon % 1 == 0 or kon == "":
                        kon = int(kon)
                    print(ch1, "/", ch2, "=", kon)
                else:
                    print("Кхе, НЕЛЬЗЯ ДЕЛИТЬ НА НОООООООЛЬ! НИИИИИИИИИИИИИИЗЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯ.")
                    print(" ")
            elif "%" in symbol or "6" in symbol:
                if ch2 != 0:
                    kon = ch1 % ch2
                    if kon % 1 == 0:
                        kon = int(kon)
                    print(ch1, "%", ch2, "=", kon)
                else:
                    print("Даже так нельзя делить на ноль(")
            else:
                print("Серьёзно? Я не знаю такого действия...(")

    otvet = a_esli()
print("Всего доброго ._.")
