if __name__ == '__main__':
    name = input('Как твое имя? ')
    age = input('Сколько тебе лет? ')
    is_love_coding = input('Тебе нравится программирование (да/нет)? ')
    my_future = input('Кем ты хочешь стать в будущем? ')

    answer = f'Меня зовут {name}. Мне {age} лет. \n ' \
             f'Нравится ли мне программирование - {is_love_coding}. ' \
             f'В будущем я хотел бы стать {my_future}.'
    print(answer)