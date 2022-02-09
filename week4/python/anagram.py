from anagram_checker import AnagramChecker

while True:
    affiche = AnagramChecker()
    word=affiche.is_valid_word(word=str(input("Entrer Un Mot:")))
    if word == 'Fin':
        print("Bye bye à la prochain")
        break
    ajouter = affiche.get_anagrams(word)
    verificateur = affiche.is_anagram(word)
    

