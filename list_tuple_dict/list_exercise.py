if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    elements_count = len(my_list)
    for index in range(elements_count):
        element_value = my_list[index]
        new_value = element_value * 10

        my_list[index] = new_value
    print(my_list)
 