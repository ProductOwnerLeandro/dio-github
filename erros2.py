# Erros 2
try:

	a = float(input("Digite o numero A: "))
	b = float(input("Digite o numero B: "))
	
	print(a/b)
except ValueError as error:
	print("Input inválido, digite apenas número")

except ZeroDivisionError as error:
	print("Divisão não pode ser feita por zero")

except Exception as error:
	print("Algum erro ocorreu")
	print(error)
		
finally:
	print("Fim do programa")
		
		
Continuar na Aula 22		
		
		
