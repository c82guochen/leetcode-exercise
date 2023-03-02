# The functions get and put must each run in O(1) average time complexity.
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.pre = self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}  #Hashmap - dictionary
        #map the key to nodes
        #left - LRU right - most recent unit
        self.left, self.right = Node(0,0), Node(0,0)
        #These two nodes are dummy node to indicate the leftmost and rightmost node
        self.left.next, self.right.pre = self.right, self.left
        #Now there is no node between left and right, so they point toeach other

    def remove(self, node):
        pre, nxt = node.pre, node.next
        pre.next, nxt.pre = nxt, pre

    def insert(self, node):
        # should insert the node to the rightmost(between right.pre and right)
        pre, nxt = self.right.pre, self.right
        pre.next = nxt.pre = node
        node.pre, node.next = pre, nxt

    def get(self, key):
        if key in self.cache:
            # update the most recent unit
            # remove the node firstly
            self.remove(self.cache[key])
            # insert the node to the rightmost
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key, value):
        if key in self.cache:
            # remove the node firstly
            self.remove(self.cache[key])
        # Here we don't want to modify the chache[key].value directly because of the encapsulation
        # create a new one and insert the node to the rightmost
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # After insertion, we need to check the cache length
        if len(self.cache) > self.cap:
            #if yes, we remove the LRU
            lru = self.left.next
            self.remove(lru)
            # delete the corresponding item in cache(dic) by del 
            del self.cache[lru.key]