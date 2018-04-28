"""Mine frequent word sets using the Aprior data mining algorithm."""

from typing import List, Tuple, Dict, Hashable

Word = Hashable
"""Alias any hashable as a word."""

WordSet = Tuple[Word]
"""Alias tuple of words as word set."""

WordSetSupport = Tuple[WordSet, int]
"""Alias tuple of word and absolute support count as word set support."""

class WordMine:
    """Structure word sets for frequency mining."""
    
    def __init__(self, wordSets: List[WordSet]):
        """Initialize new word mine from word sets.
        
        Args:
            wordSets: List of word sets.
        """
        self.__wordSets = []
        self.__wordOccurs = {}
        for wordSet in wordSets:
            self.addWordSet(wordSet)
    
    @classmethod
    def fromFile(cls, filePath: str, wordDelimeter: str=";"):
        """Initialize new word mine from from text file of word sets.
        
        Args:
            filePath: Relative path to file.
            wordDelimeter (optional): Character or characters to split read line
                into separate words. Defaults to semi-colon (";").
        
        Returns:
            List of word sets.
        """
        wordSets = []
        for line in open(filePath):
            wordSets.append(set(line.replace("\n", "").split(wordDelimeter)))
        return cls(wordSets)
    
    @property
    def wordSets(self) -> List[WordSet]:
        return self.__wordSets
    
    @property
    def countSets(self) -> int:
        return len(self.__wordSets)
    
    @property
    def words(self) -> List[Word]:
        return self.__wordOccurs.keys()
    
    @property
    def countWords(self) -> int:
        return len(self.__wordOccurs)
    
    @property
    def wordSupport(self) -> List[WordSetSupport]:
        return map(lambda wrd: (wrd, len(self.__wordOccurs[wrd])), \
                self.__wordOccurs.keys())

    def addWordSet(self, wordSet: WordSet):
        """Adds a single word set to the mine.
        
        Args:
            wordSet: A single word set.
        """
        setIndex = self.countSets
        for word in wordSet:
            self.addWordOccurence(word, setIndex)
        self.__wordSets.append(wordSet)
    
    def addWordOccurence(self, word: Word, occurredAtIndex: int):
        """Add as single word and its occurence at an index.
        
        Args:
            word: A single word.
            occurredAtIndex: The index at which the word occurred.
        """
        try:
            self.__wordOccurs[word].append(occurredAtIndex)
        except KeyError:
            self.__wordOccurs[word] = [occurredAtIndex]
    
    def getWordsWithMinimumFrequency(self, frequency: float) -> List[WordSetSupport]:
        """Return frequent words and their absolute support count.
        
        Args:
            frequency: Minimum relative frequency (expressed as a
                decimal between 0 and 1) in all word sets for a word to be
                considered "frequent".
        
        Returns:
            Dictionary of (word: absolute support count)
        """
        assert 0 <= frequency and frequency <= 1
        support = self.countSets * frequency
        if support == 0:
            return {}
        else:
            return self.getWordsWithMinimumSupport(support)
    
    def getWordsWithMinimumSupport(self, support: int) -> List[WordSetSupport]:
        """Return frequent words and their absolute support count.
        
        Args:
            support: Minimum absolute support count (expressed as an
                integer between 0 and word set count) in all word sets for a
                word to be considered "frequent".
        
        Returns:
            Dictionary of (word: absolute support count)
        """ 
        assert 0 <= support and support <= self.countSets
        if support == 0:
            return {}
        else:
            return list(filter(lambda ws: ws[1] >= support, self.wordSupport))
    
# Mine frequent words and output to file for assignment part 1
locationCategoryMine = WordMine.fromFile("categories.txt")
frequentWords = locationCategoryMine.getWordsWithMinimumFrequency(0.01)
with open("patterns-n1.txt", "w") as file:
    for line in map(lambda t:str(t[1]) + ":" + t[0], frequentWords):
        file.write("%s\n" % line)