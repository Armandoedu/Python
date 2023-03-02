#Ao adicionar o valor 10 na variavel "codigo", automaticamente ela será reconhecida como tipo inteiro
codigo = 10
nome = 'Armando'
salario = 2000.00
ativo = True

#criei uma variavel e a nomeei como tipo, nela usei a função "type()" que vai retornar o tipo da variavel
tipo = type (codigo)


print("Nome: %s"% nome)
print("Código: %d"% codigo)
print(tipo)
print("Salário: %d"% salario)
print("Ativo: %r\n\n"% ativo)

#usando apenas um "printf", para imprimir todas as variaveis em uma única linha concatenando atravez de virgula
print("Nome: ", nome, "Codigo: ", codigo, "Salario: ", salario, "Ativo/Inativo: ", ativo,"\n\n")

#outro tipo de concatenação, tirando as vírgulas e usando o sinal '+' para cocatenar, mas é preciso converter as variáveis que não são de string
#para string, para isso usamos a função "str()"
print("Nome: "+ nome+ "\tCodigo: "+ str(codigo)+ "\tSalario: "+ str(salario)+ "\tAtivo/Inativo: "+ str(ativo))

#usando a função "str()", a variável que não é uma string vai ser convertida para que seja representada de forma que seja legível para as pessoas
