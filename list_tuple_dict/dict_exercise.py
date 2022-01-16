if __name__ == '__main__':
    pupils = {'Миша': 10, 'Федя': 15, 'Гриша': 12, 
              'Ваня': 12, 'Саша': 7}
    # Самый старший и самый младший ученики
    min_age = 100
    max_age = 0
    junior_name = senior_name = ''
    for name in pupils:
        age_val = pupils[name]
        if age_val < min_age:
            junior_name, min_age = name, age_val
        if age_val > max_age:
            senior_name, max_age = name, age_val
    print(f'Самый младший ученик - {junior_name}. Его возраст - {min_age}')
    print(f'Самый старший ученик - {senior_name}. Его возраст - {max_age}')


    # Посчитаем средний возраст учеников:
    pupils_count = len(pupils)
    total_age = 0
    for age in pupils.values():
        total_age = total_age + age
    mid_age = total_age / pupils_count
    print(f'Средний возраст ученика - {mid_age}')
    # Получить имена всех учеников:
    names = []
    for name in pupils:
        names.append(name)
    print(names)
    # Исправление возраста у Феди:
    pupils['Федя'] = 10
    # Проверка исправления:
    print(pupils['Федя'])
    # Добавление ученика:
    name = 'Мария'
    age = 14
    pupils[name] = age
    # Проверка добавления
    age = pupils[name]
    print(f'Ученик {name}. Возраст {age} лет')