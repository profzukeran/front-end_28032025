def avaliar_beneficio(anos_empresa):
    if anos_empresa < 5:
        return "Aumento no vale refeição"
    elif 5 <= anos_empresa < 10:
        return "Reajuste de 10% no salário"
    elif 10 <= anos_empresa < 15:
        return "Participação na festa de comemoração"
    else:
        return "Nenhum benefício especificado para esse tempo de empresa"

# Exemplo de uso:
#anos = int(input("Digite o tempo de empresa do colaborador (em anos): "))
#beneficio = avaliar_beneficio(anos)
#print(f"Benefício concedido: {beneficio}")
