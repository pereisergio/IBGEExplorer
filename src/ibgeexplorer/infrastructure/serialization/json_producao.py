from dataclasses import dataclass
from typing import Dict, List, Type, TypeVar

T = TypeVar("T", bound="TabelaProducao")


@dataclass
class Nivel:
    id: str
    nome: str


@dataclass
class Localidade:
    id: str
    nivel: Nivel
    nome: str

    @classmethod
    def from_json(cls, data: dict) -> "Localidade":
        return cls(id=data["id"], nivel=Nivel(**data["nivel"]), nome=data["nome"])


@dataclass
class Serie:
    ano_valor: Dict[str, str]

    @classmethod
    def from_json(cls, data: dict) -> "Serie":
        return cls(ano_valor=data)


@dataclass
class SeriePorLocalidade:
    localidade: Localidade
    serie: Serie

    @classmethod
    def from_json(cls, data: dict) -> "SeriePorLocalidade":
        return cls(
            localidade=Localidade.from_json(data["localidade"]),
            serie=Serie.from_json(data["serie"]),
        )


@dataclass
class Classificacao:
    id: str
    nome: str
    categoria: Dict[str, str]

    @classmethod
    def from_json(cls, data: dict) -> "Classificacao":
        return cls(id=data["id"], nome=data["nome"], categoria=data["categoria"])


@dataclass
class Resultado:
    classificacoes: List[Classificacao]
    series: List[SeriePorLocalidade]

    @classmethod
    def from_json(cls, data: dict) -> "Resultado":
        return cls(
            classificacoes=[
                Classificacao.from_json(c) for c in data.get("classificacoes", [])
            ],
            series=[SeriePorLocalidade.from_json(s) for s in data.get("series", [])],
        )


@dataclass
class TabelaProducao:
    id: str
    variavel: str
    unidade: str
    resultados: List[Resultado]

    @classmethod
    def from_json(cls: Type[T], data: dict) -> T:
        return cls(
            id=data["id"],
            variavel=data["variavel"],
            unidade=data["unidade"],
            resultados=[Resultado.from_json(r) for r in data.get("resultados", [])],
        )

    @classmethod
    def from_json_list(cls: Type[T], data: List[dict]) -> List[T]:
        return [cls.from_json(item) for item in data]
