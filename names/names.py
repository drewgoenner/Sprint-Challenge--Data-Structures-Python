import time

#Use a Binary Search Tree to improve time
#For ease of not adding a new file and no instructions otherwise, I will build the BST here:

class BSearchTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		# if the value is greater or equal to the value of the node
		if value >= self.value:
		# if there is nothing to the right, the new node is inserted to the right
			if not self.right:
				self.right = BSearchTree(value)
		# otherwise move to the right and run insert on that node
			else:
				self.right.insert(value)
		# if the value is less than the value of the node
		elif value < self.value:
		# if nothing to the left, the new node is inserted to the left
			if not self.left:
				self.left = BSearchTree(value)
		# otherwise move to the node to the left and run insert again
			else:
				self.left.insert(value)

	def contains(self, target):
		# if the value of the node equals the target, return true
		if self.value == target:
			return true
		# if the value of the node is less than the target, check to the right
		if self.value < target:
		# if there is no node to the right, return false
			if not self.right:
				return False
		# otherwise, run contains on the node to the right and repeat until target is found, or no more nodes to the right
			else:
				return self.right.contains(target)
		# do the same as above, only moving to the left if the value of the node is greater than the target
		elif self.value > target:
			if not self.left:
				return False
			else:
				return self.left.contains(target) 


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
