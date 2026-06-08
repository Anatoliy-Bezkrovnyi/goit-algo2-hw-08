def find_min_max(arr):
    # Базовий випадок 1: тільки один елемент в масиві
    if len(arr) == 1:
        return arr[0], arr[0]  # (min, max)
    
    # Базовий випадок 2: два елементи, просто порівнюємо між собою
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]

    # тут ділимось на два постійно
    mid = len(arr) // 2
    
    # тут мені ШІ пояснив треба шукати min max на кожній ітерації
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    # тут ми підміняємо існуючі значення якщо на наступній ітерації знайшли щось менше чи більше
    current_min = left_min if left_min < right_min else right_min
    current_max = left_max if left_max > right_max else right_max

    return current_min, current_max

# Приклад:
arr = [38, 27, 43, 3, 9, 82, 10]
min_val, max_val = find_min_max(arr)

print(f"Мінімум: {min_val}")  # 3
print(f"Максимум: {max_val}")  # 82