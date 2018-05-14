#! /usr/bin/python
print "Created by Cory Noll (Null) Crimmins - Golden on May 12 08:20:32 MDT 2018"
print "Voyant assignment #2"
print "MIT License"

import sys

# Classes
class RadixNode:
    # Radix Trie node
    def __init__(self):
        # Constructor
        self.kids = {} # Table container
        self.leaf = False # A leaf is an ending to a trie branch

class RadixTrie:
    # Radix trie or tree class
    def __init__(self):
        # Constructor
        self.root = RadixNode() # "The trunk"

    def insert(self, key):
        # Traverses the tree for each char and adds nodes to the table.
        table = self.root
        keyLen = len(key)
        for i in range(0, keyLen):
            c = key[i] # Character from key
            if c not in table.kids: # If not in table, add
                table.kids[c] = RadixNode() # Create node
            if i == (keyLen - 1): # Are we at the end... do we leaf?
                table.kids[c].leaf = True
            table = table.kids[c] # Done... next char

    def remove(self, key):
        # This was totally extra and I didn't use it once...
        # Traverses the tree for each char and trims nodes for each match.
        stack = [self.root] # We need to get the path
        table = self.root
        keyLen = len(key)
        for i in range(0, keyLen):
            c = key[i] # Character from key
            if c in table.kids: # Match!
                stack += [table] # Push to stack
                table = table.kids[c] # Next char
            else:
                return False # Not found...
        if stack[-1].leaf == True: # Leaf?
            stack[-1].leaf = False # Not anymore!
            for i in range(0, keyLen):
                x = len(key) - i - 1 # Index from depth
                del stack[x].kids[key[x]] # Removed
        return True

    def contains(self, key):
        # Traverses the tree and finds a match that is a leaf.
        table = self.root
        keyLen = len(key)
        for i in range(0, keyLen):
            c = key[i] # Character from key
            if i == (keyLen - 1): # Are we at the end?
                return c in table.kids and table.kids[c].leaf # Match!
            else:
                if c in table.kids: # Found?
                    table = table.kids[c] # Next!
                else:
                    return False # Darn.
        return False # Darn.

argLength = len(sys.argv)-1 # We don't care about the script location
script = sys.argv[0] # That last line was kinda a lie... we do...

if argLength == 0:
    print "Expected:"
    print "$ " + script + " foo"
    print "Not common password"
else:
    password = sys.argv[1]
    file = open("1000MostCommonPasswords(byDavidWittman).txt", "r")
    tree = RadixTrie()
    for line in file.readlines():
        tree.insert(line[:-1]) # [:-1] removes the newline
    file.close()
    if tree.contains(password):
        print "Common password"
    else:
        print "Not common password"
