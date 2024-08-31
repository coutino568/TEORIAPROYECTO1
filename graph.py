


class Graph(object):
	
	def __init__(self, **kwargs):	

		if('states' in kwargs):
			self.states = kwargs['states']

		else:
			self.states = []


		if('initialState' in kwargs):
			self.initialState = kwargs['initialState']

		else:
			self.initialState = ""



		if('finalState' in kwargs):
			self.finalState = kwargs['finalState']

		else:
			self.endState = []


		if('transitions' in kwargs):
			self.transitions = kwargs['transitions']

		else:
			self.transitions = []






def concatenateGraphs(graph1,graph2):
	##estoy suponiendo que no se repiten nombres de estados

	graph1 = addPrefixesToGraphs(graph1,"1-")

	graph2 = addPrefixesToGraphs(graph2,"2-")

	newGraph = Graph()



	#copia todos los estados exepto el inical de la 2
	for state in graph1.states:
		newGraph.states.append(state)
	for state in graph2.states:
		if not(state==graph2.initialState):
			newGraph.states.append(state)
	newGraph.initialState=graph1.initialState
	newGraph.finalState=graph2.finalState




	#copia todas las transiciones expeto las inicales del 2, esas las susitituye por 
	newtransitions =[]
	for transition in graph1.transitions:
		newtransitions.append(transition)
	for transition in graph2.transitions:
		if transition[0]==graph2.initialState:
			newtransitions.append([graph1.finalState,transition[1],transition[2]])
		else:
			newtransitions.append(transition)


	newGraph.transitions=newtransitions

	
	return renameGraphStates(newGraph)

	##crear la transicon 
	#el final del 1 debe tener edges de todos los que tienen como origen el inicial del 2



def orGraphs(graph1,graph2):


	graph1 = addPrefixesToGraphs(graph1,"1-")
	graph2 = addPrefixesToGraphs(graph2,"2-")


	epsilonSymbol="#"

	newGraph = Graph()
	for state in graph1.states:
		newGraph.states.append(state)

	for state in graph2.states:
		newGraph.states.append(state)

	for transition in graph1.transitions:
		newGraph.transitions.append(transition)
	for transition in graph2.transitions:
		newGraph.transitions.append(transition)


	newGraph.initialState="nuevoinicial"
	newGraph.states.append("nuevoinicial")
	newGraph.finalState="nuevoFinal"
	newGraph.states.append("nuevoFinal")




	#crea las trnasiiones epsilon

	newGraph.transitions.append([newGraph.initialState,graph1.initialState,epsilonSymbol])
	newGraph.transitions.append([newGraph.initialState,graph2.initialState,epsilonSymbol])

	newGraph.transitions.append([graph1.finalState,newGraph.finalState,epsilonSymbol])
	newGraph.transitions.append([graph2.finalState,newGraph.finalState,epsilonSymbol])


	
	return renameGraphStates(newGraph)


def kleeneGraph(graph1):

	graph1 = addPrefixesToGraphs(graph1,"2-")


	epsilonSymbol="#"

	newGraph = Graph()

	#hereda los estados y transiciones
	newGraph.states = graph1.states
	newGraph.transitions = graph1.transitions


	#agruega las transiciones epsilon
	newGraph.initialState="nuevoinicial"
	newGraph.states.append("nuevoinicial")
	newGraph.finalState="nuevoFinal"
	newGraph.states.append("nuevoFinal")


	newGraph.transitions.append([newGraph.initialState,graph1.initialState,epsilonSymbol])
	newGraph.transitions.append([graph1.finalState,graph1.initialState,epsilonSymbol])
	newGraph.transitions.append([graph1.finalState,newGraph.finalState,epsilonSymbol])
	newGraph.transitions.append([newGraph.initialState,newGraph.finalState,epsilonSymbol])

	result = renameGraphStates(newGraph)
	return result



def renameGraphStates(graph1):

	newGraph = Graph()

	mappedStates =[]

	for x in range(len(graph1.states)):

		##si es estado inicial


		newname= "q"+str(x)

		currentvalue=graph1.states[x]

		##renombra las transiciones
		# for transition in graph1.transitions:
		# 	if(transition[0]==currentvalue and transition[1]==currentvalue):
		# 		newGraph.transitions.append([newname,newname,transition[2]])
		# 	elif transition[0]==currentvalue:
		# 		newGraph.transitions.append([newname,transition[1],transition[2]])
		# 	elif transition[1]==currentvalue:
		# 		newGraph.transitions.append([transition[0],newname,transition[2]])

		newGraph.states.append(newname)
		mappedStates.append([currentvalue,newname])

		##en caso que el estado este siendo definido como inicial o final
		if graph1.initialState == currentvalue:
			newGraph.initialState = newname
		if graph1.finalState == currentvalue:
			newGraph.finalState = newname



	##ahora susituir en las transicones
	for x in range(len(graph1.transitions)):
		
		oldFrom = graph1.transitions[x][0]
		oldTo = graph1.transitions[x][1]
		oldSymbol = graph1.transitions[x][2]

		newTransition=[oldFrom,oldTo,oldSymbol]

		for x in range(len(mappedStates)):
			if mappedStates[x][0]==oldFrom:
				newTransition[0]=mappedStates[x][1]

		for x in range(len(mappedStates)):
			if mappedStates[x][0]==oldTo:
				newTransition[1]=mappedStates[x][1]

		
		newGraph.transitions.append(newTransition)


	# print(mappedStates)
	# print(newGraph.states)
	# print(newGraph.transitions)
	return newGraph



def addPrefixesToGraphs(graph1,prefix):


	newGraph = Graph()
	for state in graph1.states:
		newGraph.states.append(prefix+state)

	for transition in graph1.transitions:
		newGraph.transitions.append([prefix+transition[0],prefix+transition[1],transition[2]])

	newGraph.initialState= prefix+graph1.initialState
	newGraph.finalState= prefix+graph1.finalState

	return newGraph
