class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True


    def search(self, word):
        # j is the index of word we search 
        def DFS(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    # We need to do DFS on cur.children.values() to search c in all children of cur
                    for child in cur.children.values():
                        # if c is ".", we compare word's next character and child
                        if DFS(i + 1, child):
                            # If any child can match the word, DFS returns true
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            # After for iteration, we return cur.endOfEnd
            # (which means all comparisons between word and children are done,now it's the end of word)   
            return cur.endOfWord
        # We need use the recursion to complete search algorithm
        return DFS(0, self.root)