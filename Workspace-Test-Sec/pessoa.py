class Pessoa:
    def __init__(self, nome, idade, cpf, endereco):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
        self.__endereco = endereco

    def falar(self):
        print(f"Olá, meu nome é {self.nome}")

    def andar(self):
        print(f"Agora vamos caminhar, {self.nome}")

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, novo_cpf):
        if isinstance(novo_cpf, str) and len(novo_cpf) == 14:
            self.__cpf = novo_cpf
        else:
            print("CPF inválido")

    def get_endereco(self):
        return self.__endereco
    
    def set_endereco(self, novo_endereco):
        if isinstance(endereco, str) and len(novo_endereco) == 200:
            self.__endereco = novo_endereco
        else:
            print(" endereco Inválido")
        return self._endereco

# Entrada de dados (fora da classe, usado em execução normal, não nos testes)
if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cpf = input("Digite seu CPF (formato xxx.xxx.xxx-xx): ")
    endereco = input("Digite seu endereço: ")

    p = Pessoa(nome, idade, cpf, endereco)
    p.falar()
    p.andar()

    print("CPF atual:", p.get_cpf())

    novo_cpf = input("Digite um novo CPF: ")
    p.set_cpf(novo_cpf)
    print("Novo CPF:", p.get_cpf())
    print("Endereco:", p.get_endereco())
