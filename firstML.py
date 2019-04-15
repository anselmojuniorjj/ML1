from sklearn import tree

lisa = 1
irregular = 0
maca = 1
laranja = 0

pomar = [ [150, lisa], [130, lisa], [180, irregular], [160, irregular] ]
resultado = [maca, maca, laranja, laranja]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(pomar, resultado)

peso = input("Entre com o peso: ")
superficie = input("Entre com a superficie: ")

if superficie == "lisa":
	sup = 1
else:
	sup = 0
	
resultadoUsuario = clf.predict([[peso, sup]])

if resultadoUsuario == 1:
	print("É uma maçã!")
else:
	print("É uma laranja!")