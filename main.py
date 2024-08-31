
from graph import *



import graphviz
from parser import Parser
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'


specialOperators=["(",")","|","+","*"]
epsilonSymbol="#"
expresion1 = "a+b"
expresion2 = "a+b+a"
alphabet = []

acceptanceStates=["q2"]
currentState=""

states=["q0","q1","q2"]

transitions = [["q0","q1","a"],["q0","q0","#"],["q1","q2","b"]]

for char in expresion1:
	if not(char in specialOperators):
		# es simbolo del alfabeto
		if not(char in alphabet):
			alphabet.append(char)


print(alphabet)








tree = graphviz.Digraph('AFN', comment='AFN', format='png')
# nodes= [[1,"q0"],[2,"q1"],[3,"q2"]]
# edges=[[1,2],[2,2],[2,3]]

def drawGraph(grafo):
	for state in grafo.states:
		if state == grafo.finalState:
			color ="red"
		elif state == grafo.initialState:
			color ="green"
		else:
			color= "black"
		# color = "red" if (state == grafo.finalState) else "black"
		tree.node(state,state,color=color)

	for transition in grafo.transitions:
		tree.edge(transition[0],transition[1],constraint='true',label=transition[2])









#ejemplo aa*(b|a)  seria con operaciones concatenado de a y a*; concatenado a el o de a y b

grafo1 = Graph(initialState="q0",states=["q0","q1"],finalState="q1",transitions=[["q0","q1","a"]])
grafo2 = Graph(initialState="q4",states=["q4","q5"],finalState="q5",transitions=[["q4","q5","b"]])


# drawGraph(concatenateGraphs(concatenateGraphs(grafo1,kleeneGraph(grafo1)),orGraphs(grafo1,grafo2)))






# drawGraph(renameGraphStates(grafo1))
# drawGraph(grafo2)
# drawGraph(concatenateGraphs(grafo1,grafo2))

drawGraph(concatenateGraphs(grafo1,grafo2))
# drawGraph(orGraphs(grafo1,grafo2))
# drawGraph(kleeneGraph(grafo1))


tree.render(directory='doctest-output').replace('\\', '/')


