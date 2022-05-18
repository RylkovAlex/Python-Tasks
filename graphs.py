station_graph = {"Адмиралтейская":
                     {"Садовая": 4},
                 "Садовая":
                     {"Сенная площадь": 3,
                      "Спасская": 3,
                      "Адмиралтейская": 4,
                      "Звенигородская": 5},
                 "Сенная площадь":
                     {"Садовая": 3,
                      "Спасская": 3},
                 "Спасская":
                     {"Садовая": 3,
                      "Сенная площадь": 3,
                      "Достоевская": 4},
                 "Звенигородская":
                     {"Пушкинская": 3,
                      "Садовая": 5},
                 "Пушкинская":
                     {"Звенигородская": 3,
                      "Владимирская": 4},
                 "Владимирская":
                     {"Достоевская": 3,
                      "Пушкинская": 4},
                 "Достоевская":
                     {"Владимирская": 3,
                      "Спасская": 4}}


# «алгоритм Дейкстры»

def getMinWeight(start, finish, graph):
    weight = {k: 1000 for k in graph.keys()}
    weight[start] = 0
    isWatched = {k: False for k in graph.keys()}
    P = {k: None for k in graph.keys()}  # предки

    for _ in range(len(weight)):
        # выбираем среди непросмотренных вершин наименьшую по весу ребра
        min_k = min([k for k in isWatched.keys() if not isWatched[k]], key=lambda x: weight[x])

        for sub in graph[min_k].keys():  # проходимся по всем смежным вершинам
            # weight[sub] = min(weight[sub], weight[min_k] + graph[min_k][sub])
            if weight[sub] > weight[min_k] + graph[min_k][sub]:  # если расстояние от текущей вершины меньше
                weight[sub] = weight[min_k] + graph[min_k][sub]  # то фиксируем его
                P[sub] = min_k  # и записываем как предок
        isWatched[min_k] = True  # просмотренную вершину помечаем

    pointer = finish  # куда должны прийти
    result = []
    while pointer is not None:  # перемещаемся, пока не придём в стартовую точку
        result.append(f'{pointer} : {weight[pointer]}')
        pointer = P[pointer]
    print(f'Наикротчайший путь от {start} к {finish} = {weight[finish]}.\nОн проходит через следующие вершины:')
    print('\n'.join(result[::-1]))
    return


getMinWeight('Адмиралтейская', 'Владимирская', station_graph)
