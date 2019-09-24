class Node:
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.left = None
		self.right = None
	
	def __str__(self):
		return str(self.val)


class BST:
	def __init__(self):
		self._root = None
		
	def insert(self, key, val):
		self._root = self._ins(self._root, key, val)
		
	def _ins(self, x, key, val):
		if x is None:
			return Node(key,val)
		
		if val < x.val:
			x.left = self._ins(x.left, key, val)
		elif val > x.val:
			x.right = self._ins(x.right, key, val)
		else:
			x.val = val
		
		return x

	def delete(self,val):
		self._root=self._del(self._root,val)

	def _del(self, x, val): 
		if x is None:
			raise KeyError	
        
		if val < x.val:
			x.left = self._del(x.left, val)
		elif val > x.val:
			x.right = self._del(x.right, val)
		else:
			if x.left == None:
				x = x.right
			elif x.right == None:
				x = x.left
			else:
				next = x.right
				while next.left != None:
					next = next.left
					x.key = next.key
					x.val = next.val
					x.right = self._del(x.right,x.val)
		return x
	
	def inorder(self):
		self._inorder(self._root)
	
	def _inorder(self, x):
		if x is None:
			return
		self._inorder(x.left)
		print(x.key, ' ', x.val)
		self._inorder(x.right)
		return
	
	def preorder(self):
		self._preorder(self._root)
		
	def _preorder(self,x):
		if x is None:
			print(".", end = " ")
			return
		print(x.val, end = " ")
		self._preorder(x.left)
		self._preorder(x.right)
		return


t = BST()
i = 0
while True:
	n = int(input())
	i += 1
	if n==0:
		break
	t.insert(n,n)
print()
k = int(input("Valor a deletar: "))
t.delete(k)
t.inorder()