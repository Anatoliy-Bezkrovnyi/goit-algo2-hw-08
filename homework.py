from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        
        if not isinstance(pattern, str):
            raise TypeError(f"Illegal argument for count_words_with_suffix: pattern = {pattern} must be a string")
        
        if not pattern:
            return self.size

        count = 0
        all_keys = self.keys()
        for key in all_keys:
            if key.endswith(pattern):
                count += 1
                
        return count

    def has_prefix(self, prefix) -> bool:
        
        if not isinstance(prefix, str):
            raise TypeError(f"Illegal argument for has_prefix: prefix = {prefix} must be a string")
        
        if not prefix:
            return not self.is_empty()

        # ШІ пропонує використати наступний підхід - Замість витягування всіх ключів, ми просто намагаємося 
        # пройти по дереву по символах префікса. Якщо пройшли — префікс існує.
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
            
        # Якщо ми дорулили до кінця префікса, це означає, що гілка існує.
        # Оскільки у нас при put() пусті вузли без слів не створюються, 
        # наявність цієї гілки гарантує, що далі є хоча б одне слово.
        return True

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat