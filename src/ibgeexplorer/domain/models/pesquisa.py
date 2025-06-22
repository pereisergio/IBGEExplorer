from dataclasses import dataclass, field

from ibgeexplorer.domain.models import Agregado


@dataclass
class Pesquisa:
    id: str
    nome: str
    agregados: list[Agregado] = field(default_factory=list)
