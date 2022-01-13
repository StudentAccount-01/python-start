if __name__ == '__main__': 
    my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    elements_count = len(my_tuple)
    for index in range(elements_count):
        need_index = elements_count - index - 1
        element = my_tuple[need_index]
        print(f'Элемент - {element}\tИндекс - {need_index}')
