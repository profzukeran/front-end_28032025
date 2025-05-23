def capturar_e_validar_ip(ip_digitado):
    # Verifica se o IP tem 4 partes separadas por ponto e cada parte é um número
    partes = ip_digitado.strip().split(".")
    if len(partes) == 4 and all(parte.isdigit() and 0 <= int(parte) <= 255 for parte in partes):
        return True
    return False

def consultar_pais_por_ip(ip):
    # Simulação de serviço GeoIP
    ip_para_pais = {
        "192.168.1.1": "Brasil",
        "192.168.1.2": "Brasil",
        "192.168.1.3": "Brasil",
        "192.168.1.4": "Brasil",
        "192.168.1.5": "Brasil",
        "192.168.1.6": "Brasil",
        "192.168.1.7": "Brasil",
        "192.168.1.8": "Brasil",
        "192.168.1.9": "Brasil",
        "192.168.1.10": "Brasil",
        "8.8.8.8": "Estados Unidos",
        "203.0.113.0": None  # IP sem país identificado
    }
    return ip_para_pais.get(ip, None)


def sistema():
    print("[Início] Usuário acessa o sistema")

    ip = input("Digite o IP do usuário: ")

    if not capturar_e_validar_ip(ip):
        print("Acesso bloqueado. IP inválido.")
        print("[LOG] IP inválido registrado.")
        return

    pais = consultar_pais_por_ip(ip)
    if pais is None:
        print("País não identificado.")
        print("Permissões mínimas aplicadas. Solicitação de verificação manual enviada.")
        return

    if pais != "Brasil":
        print(f"País identificado: {pais}")
        print("Funcionalidades restritas. Aviso exibido ao usuário.")
        return

    print("País permitido:", pais)
    print("Permissões aplicadas com sucesso.")
    print("Acesso concedido ao sistema.")
    print("[Fim]")

# Executar o programa
sistema()
