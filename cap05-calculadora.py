def cabecalho():
	print('\n*******************************calculadora em python*******************************')
	print('\n\nselecione a operacao:')
	print('\n1-soma')
	print('\n2-subtracao')
	print('\n3-produto')
	print('\n4-divisao')
	print('\n5-sair')
	print('\n\ndigite a opcao: ')

def soma(a, b): print(a + b)

def subtracao(a, b): print(a - b)

def produto(a, b): print(a * b)

def divisao(a, b): 
	if b == 0:
		return print('\n\nerror')
	else: 
		print(a / b)

aux = 0
while aux != 5:
	# cabecalho()
	aux = input()
	print('number1: ')
	a = input()
	print('number2: ')
	b = input()	
	print(a,b)
	if aux == 1:
		soma(a,b)
	elif aux == 2:
		subtracao(a,b)
	elif aux == 3:
		produto(a,b)
	elif aux == 4:
		divisao(a,b)
	elif aux == 5:

		print('\nleaving')

print('bye')