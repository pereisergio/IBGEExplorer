from dataclasses import dataclass


@dataclass
class Variavel:
    id: str
    nome: str
    unidade: str

    def __post_init__(self):
        if not self.id:
            raise ValueError("O campo 'id' não pode ser nulo ou vazio.")
        if not self.nome:
            raise ValueError("O campo 'nome' não pode ser nulo ou vazio.")
        if not self.unidade:
            raise ValueError("O campo 'unidade' não pode ser nulo ou vazio.")

    def __repr__(self):
        return f"Variavel(id={self.id}, nome='{self.nome}', unidade='{self.unidade}')"
