if __name__ == '__main__':
    line = input('Введите любое целое число: ')
    number = int(line)

    if number < 0:
        print(f'Число {number} является отрицательным')
    elif number == 0:
        print('Введенное число - ноль')
    else:
        print(f'Число {number} положительное')