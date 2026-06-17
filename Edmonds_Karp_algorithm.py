from collections import deque

def bfs(capacity_matrix, flow_matrix, source, sink, parent):
    visited = [False] * len(capacity_matrix)
    queue = deque([source])
    visited[source] = True

    while queue:
        current_node = queue.popleft()
        
        for neighbor in range(len(capacity_matrix)):
            # Перевірка, чи є залишкова пропускна здатність у каналі
            if not visited[neighbor] and capacity_matrix[current_node][neighbor] - flow_matrix[current_node][neighbor] > 0:
                parent[neighbor] = current_node
                visited[neighbor] = True
                if neighbor == sink:
                    return True
                queue.append(neighbor)
    
    return False

# Основна функція для обчислення максимального потоку
def edmonds_karp(capacity_matrix, source, sink):
    num_nodes = len(capacity_matrix)
    flow_matrix = [[0] * num_nodes for _ in range(num_nodes)]  # Ініціалізуємо матрицю потоку нулем
    parent = [-1] * num_nodes
    max_flow = 0

    # Поки є збільшуючий шлях, додаємо потік
    while bfs(capacity_matrix, flow_matrix, source, sink, parent):
        # Знаходимо мінімальну пропускну здатність уздовж знайденого шляху (вузьке місце)
        path_flow = float('Inf')
        current_node = sink

        while current_node != source:
            previous_node = parent[current_node]
            path_flow = min(path_flow, capacity_matrix[previous_node][current_node] - flow_matrix[previous_node][current_node])
            current_node = previous_node
        
        # Оновлюємо потік уздовж шляху, враховуючи зворотний потік
        current_node = sink
        while current_node != source:
            previous_node = parent[current_node]
            flow_matrix[previous_node][current_node] += path_flow
            flow_matrix[current_node][previous_node] -= path_flow
            current_node = previous_node
        
        # Збільшуємо максимальний потік
        max_flow += path_flow

    # Тут ШІшка розширила код з пропозицією повертати не тільки флоу а і матрицю також
    return max_flow, flow_matrix


INF = float('inf')

# після розгляду задачі та розпитування ШІшки, використовуємо підхід суперджерело-суперстік, 
# адже розрахунок потоку працює тільки для одного джерела і стоку, може матрицю можна було автоматично якось робити та по аналогії 
# з прикладом доповнив руками та перевірив ШІшкою

capacity_matrix = [
    # 0..13: Магазини
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, INF], # Магазин 1
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, INF], # Магазин 2
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, INF], # Магазин 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, INF], # Магазин 4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, INF], # Магазин 5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, INF], # Магазин 6
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, INF], # Магазин 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, INF], # Магазин 8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, INF], # Магазин 9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, INF], # Магазин 10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, INF], # Магазин 11
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, INF], # Магазин 12
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, INF], # Магазин 13
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, INF], # Магазин 14
    
    # 14..17: Склади
    [15, 10, 20,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 0], # 14: Склад 1 -> Магазини 1,2,3
    [ 0,  0,  0, 15, 10, 25,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 0], # 15: Склад 2 -> Магазини 4,5,6
    [ 0,  0,  0,  0,  0,  0, 20, 15, 10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 0], # 16: Склад 3 -> Магазини 7,8,9
    [ 0, 20, 10, 15,  5, 10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 0], # 17: Склад 4 -> Магазини 10,11,12,13,14
    
    # 18..19: Термінали
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 25, 20, 15,  0,  0,  0, 0, 0], # 18: Термінал 1 -> Склади 1,2,3
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10, 15, 30,  0,  0, 0, 0], # 19: Термінал 2 -> Склади 2,3,4
    
    # 20: Суперджерело
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, INF, INF, 0, 0],
    
    # 21: Суперстік
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 0]
]

# ШІшка скорегувала матрицю після перевірки
capacity_matrix[17] = [0]*9 + [20, 10, 15, 5, 10] + [0]*8

source = 20  # Суперджерело
sink = 21    # Суперстік

max_flow, flow_matrix = edmonds_karp(capacity_matrix, source, sink)


# А отут ШІшка малює таблицю з відповідямиб і максимальний потік
terminals = {18: "Термінал 1", 19: "Термінал 2"}
warehouses = {14: "Склад 1", 15: "Склад 2", 16: "Склад 3", 17: "Склад 4"}
shops = {i: f"Магазин {i+1}" for i in range(14)}

print(f"Максимальний потік логістичної мережі: {max_flow} одиниць.\n")

print(f"{'Термінал':<15} {'Магазин':<15} {'Фактичний Потік (одиниць)':<25}")
print("-" * 58)

# Розрахунок реального внеску кожного Терміналу в кожен Магазин через Склади
for t_idx, t_name in terminals.items():
    for s_idx, s_name in shops.items():
        allocated_flow = 0.0
        
        for w_idx, w_name in warehouses.items():
            # Скільки прийшло від цього терміналу на цей склад
            flow_from_t = flow_matrix[t_idx][w_idx]
            # Скільки пішло з цього складу в цей магазин
            flow_to_s = flow_matrix[w_idx][s_idx]
            
            if flow_from_t > 0 and flow_to_s > 0:
                # Загальний об'єм, що реально зайшов на цей склад від усіх терміналів
                total_w_in = sum(flow_matrix[t][w_idx] for t in terminals.keys())
                if total_w_in > 0:
                    # Пропорційна частка потоку конкретного терміналу у загальному міксі складу
                    share = flow_from_t / total_w_in
                    allocated_flow += flow_to_s * share
                    
        if allocated_flow > 0:
            # Форматований вивід рядка таблиці
            print(f"{t_name:<15} {s_name:<15} {round(allocated_flow, 1):<25}")