class Cliente:

    def __init__(self, username, password, nome, sobrenome, cep, orcamento:float=75):
        self.username=username
        self.password=password
        self.nome=nome
        self.sobrenome=sobrenome
        self.cep=cep
        self.orcamento = orcamento
        pass