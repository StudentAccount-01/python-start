if __name__ == '__main__':
    names = {'Саша': 'м', 'Маша': 'ж', 'Женя': 'ж', 'Семен': 'м', 
             'Лена': 'ж', 'Оля': 'ж', 'Вова': 'м', 'Дима': 'м',
             'Толя': 'м', 'Катя': 'ж'}
    times = [12, 15, 11, 10, 11, 10, 14, 16, 18, 13]
    male_min_time = female_min_time = 1000
    male_winner = female_winner = 'No-name'
    # Писать код после этой строки!
    index = 0
    for name in names:
        if names[name] == 'м':
            is_male = True
        else:
            is_male = False

        time_value = times[index]

        if is_male:
            if time_value < male_min_time:
                male_winner = name
                male_min_time = time_value
        else:
            if time_value < female_min_time:
                female_winner = name
                female_min_time = time_value
        index += 1
    print(f'Самый быстрый ученик - {male_winner}')
    print(f'Самая быстрая ученица - {female_winner}')
