from hashtable import HashTable


class WordJumble:
    def __init__(self):
        self.word_table = HashTable()
        self.sort_all_words()
    
    def sort_all_words(self):
        with open ('/usr/share/dict/words') as f:
            words = f.read()
            words_list = words.split()
            for word in words_list:
                sorted_characters = sorted(word)
                sorted_word = ''.join(sorted_characters)
                self.word_table.set(sorted_word, word)
    
    def solve(self, jumble):
        if jumble is not None:
            assert isinstance(jumble, str)
        else:
            raise KeyError('jumble is not a string')
        sorted_word = ''.join(sorted(jumble))
        found_word = self.word_table.get(sorted_word)
        return found_word




if __name__ == '__main__':
    jumble = WordJumble()
    print(jumble.solve('bureek'))
    print(jumble.solve('laisa'))
    print(jumble.solve('prouot'))
    print(jumble.solve('laurr'))