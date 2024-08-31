

class Stack(object):


	def __init__(self):
		self.content=[]



	def push(self,element):
		self.content.append(element)

	def peek(self):
		if len(self.content)>0:
			return self.content[len(self.content)-1]
		else:
			return ""


	def isEmpty(self):
		if len(self.content)>0:
			return False

		else:
			return True


	def pop(self):


		head = self.content[len(self.content)-1]
		self.content = self.content[0:len(self.content)-1]

		return head

