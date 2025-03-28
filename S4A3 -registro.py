# Programa que verifica a categoria de um usuário com base na idade

# Entrada: o usuário informa a idade
idade = int(input("Digite sua idade: "))

# Estrutura condicional para determinar a categoria
if idade < 12:  
    # Se a idade for menor que 12, a pessoa é classificada como criança
    print("Você é uma criança.")
elif 12 <= idade < 18:  
    # Se a idade estiver entre 12 e 17, a pessoa é classificada como adolescente
    print("Você é um adolescente.")
elif 18 <= idade < 60:
    # Se a idade estiver entre 18 e 59, a pessoa é classificada como adulta
    print("Você é um adulto.")
else:
    # Se nenhuma das condições anteriores for atendida, a pessoa é classificada como idosa
    print("Você é um idoso.")
