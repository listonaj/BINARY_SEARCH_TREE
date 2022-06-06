from BST import *

# Creating a new Binary Search Tree
newBST = BSTNode(None)

# TEST INSERTION IN THE BINARY SEARCH TREE 
print("\nTesting some insertion into my binary search tree")
# the first one becomes the root node
print(insertNode(newBST, 70))
print(f"I confirm that the value {newBST.data} is now part of the binary search Tree")
# the value is smaller, left child of the root
print(insertNode(newBST,50))
print(f"I confirm that the node with value {newBST.leftChild.data} is now is now part of the binary search tree")
print(insertNode(newBST,90))
print(insertNode(newBST, 30))
print(insertNode(newBST,60))
print(insertNode(newBST,80))
print(insertNode(newBST,100))
print(insertNode(newBST,20))
print(insertNode(newBST,40))



