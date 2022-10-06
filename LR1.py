import sys
import math
def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    while True:
        try:
            # Пробуем прочитать коэффициент из командной строки
            coef_str = sys.argv[index]
        except:
            # Вводим с клавиатуры
            print(prompt)
            coef_str = input()
            # Переводим строку в действительное число
        try:
            coef = float(coef_str)
            break
        except ValueError:
            print("Введите заново")
    return coef

while True:
    print("Введите коэффициенты для уравнения")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    discr = b ** 2 - 4 * a * c
    print("Дискриминант D = %.2f" % discr)
    if discr >= 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print('x1 = ' + str(x1))
        print('x2 = ' + str(x2))
        if x1>=0:
            x3=math.sqrt(x1)
            print('x3 = ' + str(x3))
            print('x3 = -' + str(x3))
        if x2>=0:
            x4=math.sqrt(x2)
            print('x4 = ' + str(x4))
            print('x4 = -' + str(x4))
        break;
    else:
        print("Дискриминант отрицателен. Попробуйте еще раз.")
        


