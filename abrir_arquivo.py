try:
	
	with open('emails.txt', 'a') as arquivo:
		arquivo.write('ARquivo\n')
		
except FileNotFoundError:
		print('Arquivo não encontrado')

# r - abre arquivo para ler	
# w - abre arquivo para escrever / sobrescrever
# r - abre arquivo para excrever incrementando ao final
