#! /usr/bin/python
print "Created by Cory Noll (Null) Crimmins - Golden on May 13 14:08:04 MDT 2018
print "Voyant assignment #2"
print "MIT License"

import sys

# Classes
class RadixNode:
    # Radix Trie node
    def __init__(self):
        # Constructor
        self.kids = {}
        self.leaf = False

class RadixTrie:
    # Radix trie or tree class
    def __init__(self):
        # Constructor
        self.root = RadixNode()

    def insert(self, key):
        # Traverses the tree and finds a nice place to put a node
        table = self.root
        for i in range(0, len(key)):
            c = key[i]
            if c not in table.kids:
                table.kids.update({c: RadixNode()})
            if i == (len(key) - 1):
                table.kids[c].leaf = True
            table = table.kids[c]

    def remove(self, key):
        # Traverses the tree and removes a node.
        stack = [self.root]
        table = self.root
        for i in range(0, len(key)):
            c = key[i]
            if c in table.kids:
                table = table.kids[c]
                stack += [table]
            else:
                return False
        if stack[-1].leaf == True:
            stack[-1].leaf = False
            for i in range(0, len(key)):
                x = len(key) - i - 1
                c = key[x]
                del stack[x].kids[c]
        return True

    def contains(self, key):
        # Traverses the tree and finds a match.
        table = self.root
        for i in range(0, len(key)):
            c = key[i]
            if i == (len(key)-1):
                return c in table.kids and table.kids[c].leaf
            else:
                if c in table.kids:
                    table = table.kids[c]
                else:
                    return False
        return False

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
        tree.insert(line[:-1]) # removes the newline
    file.close()
    if tree.contains(password):
        print "Common password"
    else:
        print "Not common password"
