from sklearn import tree

irregular = 0
lisa = 1

redonda = 2
comprida = 3

vermelha = 4
alaranjada = 5
amarela = 6
verde = 7

pequena = 8
media = 9
grande = 10

# ---------------------------------------
laranja = 0
maca = 1
banana = 2
melancia = 3
# --------------------------------------

pomar = [ [redonda, lisa, vermelha, pequena], [redonda, irregular, alaranjada, pequena],
[comprida, lisa, amarela, pequena], [redonda, lisa, verde, grande] ]
resultado = [maca, laranja, banana, melancia]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(pomar, resultado)

print("Escolha entre 4 frutas:\n")
print("Banana, laranja, maçã ou melancia\n")
print("Responda as perguntas de acordo com a fruta que você escolheu.")
formato = input("Ela tem o formato redondo ou comprido? ")
superficie = input("Ela tem a superfície lisa ou rugosa? ")
cor = input("Qual a cor de sua casca? ")
tamanho = input("Ela é pequena, média ou grande? ")

if formato == "redondo" or "redonda":
	forma = 2
else:
	forma = 3

if superficie == "lisa":
	sup = 1
else:
	sup = 0
	
if cor == "vermelha":
	color = 4
elif cor == "laranja":
	color = 5
elif cor == "amarela":
	color = 6
elif cor == "verde":
	color = 7

if tamanho == "pequeno" or "pequena":
	tam = 8
elif tamanho == "medio" or "media":
	tam = 9
else:
	tam = 10
	
resultadoUsuario = clf.predict([[forma, sup, color, tam]])

if resultadoUsuario == 1:
	print("Você escolheu uma maçã!")
elif resultadoUsuario == 0:
	print("Você escolheu uma laranja!")
elif resultadoUsuario == 2:
	print("Você escolheu uma banana!")
else:
	print("Você escolheu uma melancia!")