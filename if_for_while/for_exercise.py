if __name__ == '__main__':
    lines_count = 10
    for line_index in range(lines_count):
        new_index = lines_count - line_index
        if new_index < 5:
            print(f'Это строка с номером {new_index}')
