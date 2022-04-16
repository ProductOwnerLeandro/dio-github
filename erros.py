# Erros

def divisao(a, b):
	try:
		print(a/b)
	except Exception as e:
		print("Divisão inválida")
		print(e)
divisao(20, 0)
