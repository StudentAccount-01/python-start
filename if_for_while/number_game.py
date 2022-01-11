import random


NUMBER_LIMIT = 0, 10


def generate_number() -> int:
    return random.randint(*NUMBER_LIMIT)


if __name__ == '__main__':
    unknown_number = generate_number()
    
    # Код пишем только после этой строки
    

