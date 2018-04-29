"""Mine frequent word sets using the Aprior data mining algorithm."""

from itertools import combinations
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
        return list(((k,), len(v)) for k,v in self.__wordOccurs.items())

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
    
    def getWordsWithMinimumFrequency(self, frequency: float) \
            -> List[WordSetSupport]:
        """Return frequent words and their absolute support count.
        
        Args:
            frequency: Minimum relative frequency - expressed as a
                decimal between (0, 1] - in all occurences for a word to be
                considered "frequent".
        
        Returns:
            List of (word set, absolute support count)
        """
        assert 0 < frequency and frequency <= 1
        support = self.countSets * frequency
        if support == 0:
            return {}
        else:
            return self.getWordsWithMinimumSupport(support)
    
    def getWordsWithMinimumSupport(self, support: int) -> List[WordSetSupport]:
        """Return frequent words and their absolute support count.
        
        Args:
            support: Minimum absolute support count - expressed as an
                integer between [1, word set count] - in all occurences for a
                word to be considered "frequent".
        
        Returns:
            List of (word set, absolute support count)
        """ 
        assert 0 < support and support <= self.countSets
        return list(filter(lambda ws: ws[1] >= support, self.wordSupport))

    def getWordSetsWithMinimumFrequency(self, frequency: float, \
            setSizeLimit: int = None) -> List[WordSetSupport]:
        """Return frequent words sets and their absolute support count.
        
        Args:
            frequency: Minimum relative frequency - expressed as a
                decimal between (0, 1] - in all occurences for a word set to be
                considered "frequent".
        
        Returns:
            List of (word set, absolute support count)
        """
        assert 0 < frequency and frequency <= 1
        support = self.countSets * frequency
        if support == 0:
            return {}
        else:
            return self.getWordSetsWithMinimumSupport(support, setSizeLimit)


    def getWordSetsWithMinimumSupport(self, support: int, \
            setSizeLimit: int = None) -> List[WordSetSupport]:
        """Return frequent word sets and their absolute support count.
        
        Args:
            support: Minimum absolute support count - expressed as an
                integer between [1, word set count] - in all occurences for a
                word to be considered "frequent".
        
        Returns:
            List of (word set, absolute support count)
        """
        # Set maximum set size to word count if None
        setSizeLimit = self.countWords if setSizeLimit is None else setSizeLimit
        
        # Initialize frequent word sets from frequent words
        frequentWordSets = self.getWordsWithMinimumSupport(support)
        
        # Return if only frequent words
        if setSizeLimit == 1: return frequentWordSets
        
        # Get current word sets (i.e., drop support count)
        currentWordSets = sorted(wordSet[0] for wordSet in frequentWordSets)
        
        # Iterate until size limit reached or no current word sets
        for setSize in range(2, setSizeLimit + 1):
            if len(currentWordSets) == 0: break
            
            # Get next word sets
            nextWordSets = WordMine.__getNextWordSets(currentWordSets)
            
            # Find intersection for words in each set adding to frequent word
            # sets if greater than or equal to minimum support
            currentWordSets = []
            for wordSet in nextWordSets:
                occurs = self.__wordOccurs[wordSet[0]]
                for word in wordSet[1:]:
                    occurs = set(occurs) & set(self.__wordOccurs[word])
                if len(occurs) > support:
                    currentWordSets.append(wordSet)
                    frequentWordSets.append((wordSet, len(occurs)))
        
        # Return frequent word sets
        return frequentWordSets
    
    @staticmethod
    def __getNextWordSets(currentWordSets: List[WordSet]) -> List[WordSet]:
        """Return a slightly optimistic set of next word sets from current.
        
        Example:
            [("a", "b"), ("a", "c")] returns [("a", "b", "c")] which is not a
            next possible word set since "b" and "c" did not occur together.
            However, sufficiently close to avoid final scan.
        
        Args:
            currentWordSets: List of current word sets.
        
        Returns:
            Next potential word sets.
        """
        # Return all 2-word combinations if current set size is one
        if len(currentWordSets[0]) == 1:
            return list(combinations((w[0] for w in currentWordSets), 2))
        
        # Hash words sets to their first (current set length - 1) elements
        potentials = {}
        for wordSet in currentWordSets:
            head, tail = wordSet[:-1], wordSet[-1]
            try:
                potentials[head].append(tail)
            except KeyError:
                potentials[head] = [tail]
        
        # Accumulate final next word sets from potentials with multiple tail
        # words (i.e., head found in more than one word set)
        nextWordSets = []
        for head, tail in potentials.items():
            if len(tail) < 2: continue
            
            # Create ordered combinations of tail word pairs
            for tailPairs in combinations(sorted(tail), 2):
                nextWordSets.append(head + tailPairs)
        
        # Return next word sets
        return nextWordSets


# Mine frequent words and output to file for assignment part 1
locationCategoryMine = WordMine.fromFile("categories.txt")
# frequentWords = locationCategoryMine.getWordsWithMinimumFrequency(0.01)
# with open("patterns-n1.txt", "w") as file:
#     for line in map(lambda t:str(t[1]) + ":" + ";".join(t[0]), frequentWords):
#         file.write("%s\n" % line)

# Mine frequent word sets and output to file for assignment part 2
frequentWordSets = locationCategoryMine.getWordSetsWithMinimumFrequency(0.01)
with open("patterns-nAll.txt", "w") as file:
    for line in map(lambda t:str(t[1]) + ":" + ";".join(t[0]), frequentWordSets):
        file.write("%s\n" % line)