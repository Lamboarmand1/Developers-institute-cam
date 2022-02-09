class AnagramChecker:
    def __init__(self):
        self.file = ['developpeur','laptop','pc','logiciel','telephone','programme']
    def is_valid_word(self,word):
        for x in self.file:
            if word in x:
                return word   
        else:
            return("je connais pas ce mot")    
    def get_anagrams(self, word):
        list = []
        for mots in self.file:
            if sorted(mots) == sorted(word):
                list.append(mots)
                print(list)
        return list
    def is_anagram(self, word):
        if len(word) == len(self.file) and sorted(word) == sorted(self.file):
            return True
        else:
            return False    


