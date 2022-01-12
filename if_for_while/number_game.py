if __name__ == '__main__':
    _ = input('Загадай число и нажми клавишу Enter')

    min_number = 1
    max_number = 100
    step_count = 0
    while max_number - min_number > 1:
        mean_number = (min_number + max_number) // 2
        
        user_answer = input(f'Твое число меньше {mean_number}? (y/n): ')
        if user_answer == 'y':
            max_number = mean_number
            step_count += 1
        elif user_answer == 'n':
            min_number = mean_number
            step_count += 1
        else:
            print('Введен неправильный символ. Повторите ответ на вопрос еще раз')
    else:
        user_answer = input(f'Твое число - {min_number}? (y/n): ')
        step_count += 1
        if user_answer == 'n':
            print(f'Твое число - {max_number}')
        else:
            print(f'Твое число - {min_number}')
        print(f'Количество ходов - {step_count}')
