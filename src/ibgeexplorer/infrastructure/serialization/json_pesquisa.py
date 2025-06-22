from dataclasses import dataclass
from typing import TypeVar

T = TypeVar("T", bound="TabelaPesquisa")


@dataclass
class Agregado:
    id: str
    nome: str


@dataclass
class TabelaPesquisa:
    id: str
    nome: str
    agregados: list[Agregado]

    @classmethod
    def from_json(cls: type[T], data: list[dict]) -> list[T]:
        return [
            TabelaPesquisa(
                id=grupo["id"],
                nome=grupo["nome"],
                agregados=[Agregado(**agreg) for agreg in grupo["agregados"]],
            )
            for grupo in data
        ]
