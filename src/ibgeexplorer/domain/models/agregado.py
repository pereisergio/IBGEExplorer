from dataclasses import dataclass, field

from ibgeexplorer.domain.models import Classificacao, Variavel


@dataclass
class Agregado:
    id: str
    nome: str
    classificacoes: list[Classificacao] = field(default_factory=list)
    variaveis: list[Variavel] = field(default_factory=list)

    def __post_init__(self):
        if self.id is None:
            raise ValueError("O campo 'id' não pode ser nulo.")
        if not self.nome:
            raise ValueError("O campo 'nome' não pode ser nulo ou vazio.")
