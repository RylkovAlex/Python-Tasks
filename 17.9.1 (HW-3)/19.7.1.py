def input_list(mapper, condition, message, condition_error_message, error_message):
    while True:
        try:
            list_ = list(map(mapper, input(message).split()))
            if not condition(list_):
                print(condition_error_message)
                continue
            return list_
        except ValueError:
            print(error_message)
    print(list_)


def input_number(message, error_message):
    while True:
        try:
            string = input(message)
            return float(string) if '.' in string else int(string)
        except ValueError:
            print(error_message)


def merge_sort(array):
    if (len(array) <= 1):
        return [*array]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        result = []
        i = j = 0
        while i < len(left) or j < len(right):
            if i == len(left):
                result.append(right[j])
                j += 1
                continue
            if j == len(right):
                result.append(left[i])
                i += 1
                continue
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        return result


def binary_search(list_, el):
    if len(list_) <= 1:
        return None
    l = [*list_]
    index = 0
    while len(l) >= 1:
        length = len(l)
        middle = length // 2

        if length == 1:
            position = middle + index
            next = position + 1
            if next < len(list_):
                return position if list_[position] < el and list_[next] >= el else None
            else:
                return None
        elif (l[middle] >= el):
            l = l[:middle]
        else:
            index += middle
            l = l[middle::]


list_ = input_list(
    lambda x: float(x) if '.' in x else int(x),
    lambda l: len(l) >= 2,
    'Введите последовательность чисел через пробел:\n',
    'Введите хотябы 2 числа',
    'Введённые значения не соответствуют условию. Попробуйте ещё раз!'
)
sorted_list = merge_sort(list_)

number = input_number('Введите любое число:\n', 'Введённое значения не является числом. Попробуйте ещё раз!')

position = binary_search(sorted_list, number)

if position != None:
    print(f'''В отсортированном списке {sorted_list[position]} является элементом на позиции {position}, для которого выполняется следующее условие:
он меньше введенного вами числа, а следующий за ним ({sorted_list[position + 1]}) больше или равен этому числу.''')
else:
    print(
        'В списке не найден элемент для которого выполняется следующее условие: он меньше введенного вами числа, а следующий за ним больше или равен этому числу.')
