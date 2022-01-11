if __name__ == '__main__':
    line = input('Введите исходное число: ')
    number = int(line)
    while number > 0:
        new_value = number - 1
        print(f'{new_value} = {number} - 1')
        number = new_value