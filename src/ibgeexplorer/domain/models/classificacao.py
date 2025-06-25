from dataclasses import dataclass, field

from ibgeexplorer.domain.models.categoria import Categoria


@dataclass
class Classificacao:
    id: str
    nome: str
    produtos: list[Categoria] = field(default_factory=list)

    def __post_init__(self):
        if not self.id:
            raise ValueError("O campo 'id' não pode ser nulo ou vazio.")
        if not self.nome:
            raise ValueError("O campo 'nome' não pode ser nulo ou vazio.")

    def __repr__(self):
        return f"Classificacao(id={self.id}, nome='{self.nome}')"
