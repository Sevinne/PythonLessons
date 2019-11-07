name = input("Digite o Caminho do Arquivo: ")
arq = open(name,'r')
texto = arq.read()
x = texto.split()


dict = {}
for palavra in x:
   if palavra not in dict:
     dict[palavra] = 1
   else:
     dict[palavra] += 1

soma = 0

for palavra in x:
    if dict[palavra] > soma: 
      soma = dict[palavra]
      letras = palavra


print(str(dict))
print('A Palavra mais usada: ', letras, ', Seu Uso: ', soma)