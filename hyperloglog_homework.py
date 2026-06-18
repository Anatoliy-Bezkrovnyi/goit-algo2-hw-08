import time
from datasketch import HyperLogLog

def load_data_from_file(filepath):
    """Читає файл лінія за лінією, прибираючи зайві пробіли."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Помилка: Файл {filepath} не знайдено.")
        return []

# Підрахунок за допомогою set
def count_exact_cardinality(data_list):
    start_time = time.perf_counter()
    
    unique_set = set(data_list)
    cardinality = len(unique_set)
    
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return float(cardinality), execution_time

# Підрахунок за допомогою HyperLogLog
def count_hll_cardinality(data_list, p=14):
   
    start_time = time.perf_counter()
    
    hll = HyperLogLog(p=p)
    for item in data_list:
        hll.update(item.encode('utf-8'))
    cardinality = hll.count()
    
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return float(cardinality), execution_time


if __name__ == "__main__":

    file_path = "lms-stage-access.log"
    data = load_data_from_file(file_path)
    
    if data:
        print(f"Завантажено елементів з файлу: {len(data)}")
        print("Виконується розрахунок...\n")        
        
        exact_count, exact_time = count_exact_cardinality(data)
        hll_count, hll_time = count_hll_cardinality(data)
        
        print("Результати порівняння:")
        print(f"{'':<25} {'Точний підрахунок':<20} {'HyperLogLog':<15}")
        print(f"{'Унікальні елементи':<25} {exact_count:<20.1f} {hll_count:<15.1f}")
        print(f"{'Час виконання (сек.)':<25} {exact_time:<20.4f} {hll_time:<15.4f}")