#!/usr/bin/python
from tree import Node

def preOrder(node):
	if node:
		print node.data,
		preOrder(node.left)
		preOrder(node.right)
		
def inOrder(node):
	if node:
		inOrder(node.left)
		print node.data,
		inOrder(node.right)
		
def postOrder(node):
	if node:
		postOrder(node.left)
		postOrder(node.right)
		print node.data,
		
a = Node(5)
a.left = Node(4)
a.right = Node(6)

preOrder(a)
print
inOrder(a)
print
postOrder(a)
