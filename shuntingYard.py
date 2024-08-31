

specialOperators=["(",")","|","+","*"]
epsilonSymbol="#"

from stack import Stack

def infixToPostFix(expresionOriginal):

	concatenatesymbol="."

	myStack = Stack()

	for char in expresionOriginal:
		print(char)



	expresionFinal = ""


	return expresionFinal







def checkPrecedence(char):


	#no representa mas, represetna kleene positivo
	if char == "+":
		return 1
		##simbolo para concatenar
	elif char == ".":
		return 1

	#no representa multiplicacion , representa kleene
	elif char == "*":
		return 2

	elif char == "(":
		return 2

	elif char == ")":
		return 2


# stackcito = Stack()
# expresion=("aaab")
# print(stackcito.peek())
# stackcito.push("5")
# stackcito.push("8")
# print(stackcito.peek())

# stackcito.pop()
# print(stackcito.peek())
# print(stackcito.isEmpty())
