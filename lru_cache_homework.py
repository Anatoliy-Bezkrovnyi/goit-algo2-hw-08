import random
import time
from collections import OrderedDict

# Хотів реалізувати через @lru_cache декоратор, тта не вийшло, і через консультації з ШІ прийшов
# до кастомної реалізації. Саме черерез інвалідації окремих ключів під час Update
class LRUCache:
    def __init__(self, capacity: int = 1000):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1        
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:            
            self.cache.popitem(last=False)

    def invalidate_index(self, index: int):        
        keys_to_remove = [key for key in self.cache.keys() if key[0] <= index <= key[1]]
        for key in keys_to_remove:
            del self.cache[key]

# Версії БЕЗ кешуванням 
def range_sum_no_cache(array, left, right):
    return sum(array[left:right + 1])

def update_no_cache(array, index, value):
    array[index] = value

# Версії З кешуванням 
def range_sum_with_cache(array, left, right, cache: LRUCache):
    key = (left, right)
    cached_result = cache.get(key)
    
    if cached_result != -1:
        return cached_result    
 
    result = sum(array[left:right + 1])
    cache.put(key, result)
    return result

def update_with_cache(array, index, value, cache: LRUCache):
    array[index] = value   
    cache.invalidate_index(index)


def make_queries(n, q, hot_pool=30, p_hot=0.95, p_update=0.03):
    hot = [(random.randint(0, n//2), random.randint(n//2, n-1))
           for _ in range(hot_pool)]
    queries = []
    for _ in range(q):
        if random.random() < p_update:        # ~3% запитів — Update
            idx = random.randint(0, n-1)
            val = random.randint(1, 100)
            queries.append(("Update", idx, val))
        else:                                 # ~97% — Range
            if random.random() < p_hot:       # 95% — «гарячі» діапазони
                left, right = random.choice(hot)
            else:                             # 5% — випадкові діапазони
                left = random.randint(0, n-1)
                right = random.randint(left, n-1)
            queries.append(("Range", left, right))
    return queries


if __name__ == "__main__":
    N = 100000
    Q = 50000
    
    # Масиви для тестування ідентичні
    array_no_cache = [i for i in range(N)]
    array_with_cache = [i for i in range(N)]
    
    # Список запитів до однакових масивів
    queries = make_queries(N, Q)

    #Тестування БЕЗ кешу
    start_no_cache = time.perf_counter()
    for query in queries:
        if query[0] == "Range":
            _, L, R = query
            range_sum_no_cache(array_no_cache, L, R)
        elif query[0] == "Update":
            _, idx, val = query
            update_no_cache(array_no_cache, idx, val)
    end_no_cache = time.perf_counter()
    time_no_cache = end_no_cache - start_no_cache

    # Тестування З кешем
    lru_cache_system = LRUCache(capacity=1000)
    
    start_with_cache = time.perf_counter()
    for query in queries:
        if query[0] == "Range":
            _, L, R = query
            range_sum_with_cache(array_with_cache, L, R, lru_cache_system)
        elif query[0] == "Update":
            _, idx, val = query
            update_with_cache(array_with_cache, idx, val, lru_cache_system)
    end_with_cache = time.perf_counter()
    time_with_cache = end_with_cache - start_with_cache

    # Результати тестування
    speedup = time_no_cache / time_with_cache if time_with_cache > 0 else 0
    
    print("Результати порівняння:")
    print(f"Без кешу :  {time_no_cache:.2f} c")
    print(f"LRU-кеш  :  {time_with_cache:.2f} c  (прискорення ×{speedup:.1f})")