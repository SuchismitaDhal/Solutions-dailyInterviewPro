# APPLE
"""
    SOLVED -- LEETCODE#146
    LRU cache is a cache data structure that has limited space, 
    and once there are more items in the cache than available space, 
    it will preempt the least recently used item. 
    What counts as recently used is any item a key has 'get' or 'put' called on it.

    Implement an LRU cache class with the 2 functions 'put' and 'get'. 
    'put' should place a value mapped to a certain key, and preempt items if needed. 
    'get' should return the value for a given key if it exists in the cache, and return None if it doesn't exist.
"""


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class LRUCache:
    def __init__(self, space):
        self.cap = space
        self.hash = dict()
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, key):
        if key in self.hash:
            self.handle_cache(key)
            return self.hash[key].val
        else:
            return None

    def put(self, key, value):
        if key in self.hash:
            self.hash[key].val = value
        else:
            new = Node(key, value)
            self.hash[key] = new
            if self.length == 0:
                self.head = new
                self.tail = new
            else:
                new.right = self.head
                self.head.left = new
                self.head = new
            self.length += 1
        self.handle_cache(key)

    def handle_cache(self, key):
        if self.length == self.cap + 1:
            #print('overflow at insertion key ', key)
            res = self.tail
            self.tail = self.tail.left
            self.tail.right = None
            self.length = self.cap
            del self.hash[res.key]

        else:
            trans = self.hash[key]
            if trans.left == None:
                return
            elif trans.right == None:
                self.tail = self.tail.left
                self.tail.right = None
            else:
                trans.right.left = trans.left
                trans.left.right = trans.right
            trans.right = self.head
            trans.left = None
            self.head.left = trans
            self.head = trans


cache = LRUCache(2)

cache.put(3, 3)
cache.put(4, 4)
print(cache.get(3))
# 3
print(cache.get(2))
# None

cache.put(2, 2)

print(cache.get(4))
# None (pre-empted by 2)
print(cache.get(3))
# 3
