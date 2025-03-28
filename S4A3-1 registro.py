class ContaBancaria:  # Definição da classe (representa um objeto do mundo real)
    def __init__(self, titular, saldo=0.0):
        """Construtor: Inicializa os atributos do objeto"""
        self.titular = titular  # Atributo de instância (encapsula o nome do titular)
        self.saldo = saldo  # Atributo de instância (encapsula o saldo da conta)

    def depositar(self, valor):
        """Método: Adiciona dinheiro à conta (interage com o saldo)"""
        if valor > 0:
            self.saldo += valor  # Modifica o saldo do objeto
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        """Método: Retira dinheiro da conta se houver saldo suficiente"""
        if 0 < valor <= self.saldo:
            self.saldo -= valor  # Atualiza o saldo do objeto
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def exibir_saldo(self):
        """Método: Mostra o saldo atual da conta"""
        print(f"Titular: {self.titular} | Saldo: R${self.saldo:.2f}")

# Instanciação: Criamos um objeto da classe ContaBancaria (João Silva tem uma conta)
conta1 = ContaBancaria("João Silva", 500)

# Chamando métodos para interagir com os atributos encapsulados
conta1.exibir_saldo()  # Exibe o saldo inicial
   conta1.depositar(200)  # Deposita dinheiro na conta
conta1.sacar(150)  # Realiza um saque
conta1.exibir_saldo()  # Exibe o saldo atualizado
