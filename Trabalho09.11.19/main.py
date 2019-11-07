name = input("Digite o Caminho do Arquivo: ")
files = open(name,'r')
text = files.read()
textWords = text.split()
stopWords = open('stopwords','r')
stopReads = stopWords.read()
nonWords = stopReads.split()
##
indexNon = []
dict = {}
for nonWords in textWords:
  indexNon.append(textWords.index(nonWords))

for words in textWords:
   if words not in dict:
     dict[words] = 1
   else:
     dict[words] += 1

soma = 0
##verificação qtd palavra
for words in textWords:
    if dict[words] > soma: 
      soma = dict[words]
      letras = words



print(dict)
print('A Palavra mais usada: ', letras, ', Uso: ', soma)