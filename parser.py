





class Parser(object):
	def __init__(self,filename):

		with open(filename, "r") as file:
			self.lines= file.read().splitlines()
        

		# for line in lines:
		# 	print(line)    
		
		