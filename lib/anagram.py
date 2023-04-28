# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, anagrams):
        # matches = []
        # for possible_match in anagrams:
        #     if len(self.word) == len(possible_match) and set(self.word) == set(possible_match):
        #         matches.append(possible_match)
        # return matches
        return [match for match in anagrams if len(self.word) == len(match) and set(self.word) == set(match)]
    
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))