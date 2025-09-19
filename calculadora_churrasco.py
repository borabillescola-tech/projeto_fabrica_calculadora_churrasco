# Crie um programa que calcule a quantidade de bebidas e de carne
# Para a organização de um churrasco

# Etapas
# Solicitar o número de convidados
# Criar uma função para calcular a quantidade total de bebidas
# Criar uma função para calcular a quantidade total de carne
# Apresentar o resultado com os valores de total de carne e bebidas a serem comprados

convidados = int(input("Digite o número de convidados: "))
def calcular_bebidas(convidados):
    if convidados <= 10:
        return convidados * 1.5  # litros
    elif convidados <= 20:
        return convidados * 2  # litros
    else:
        return convidados * 2.5  # litros
    
def calcular_carne(convidados):
    if convidados <= 10:
        return convidados * 0.4  # kg
    elif convidados <= 20:
        return convidados * 0.5  # kg
    else:
        return convidados * 0.6  # kg
    
print(f"Total de bebidas a serem compradas: {calcular_bebidas(convidados):.2f} litros")
print(f"Total de carne a ser comprada: {calcular_carne(convidados):.2f} kg")
