from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Type, TypeVar

T = TypeVar("T", bound="TabelaAgregado")


@dataclass
class Periodicidade:
    frequencia: str
    inicio: Optional[int] = None
    fim: Optional[int] = None
    periodos: List[str] = field(init=False)


@dataclass
class NivelTerritorial:
    Administrativo: List[str]
    Especial: List[str]
    IBGE: List[str]


@dataclass
class Variavel:
    id: int
    nome: str
    unidade: str
    sumarizacao: List[str]


@dataclass
class Categoria:
    id: int
    nome: str
    unidade: Optional[str]
    nivel: int


@dataclass
class Classificacao:
    id: int
    nome: str
    sumarizacao: Dict[str, Any]
    categorias: List[Categoria]


@dataclass
class TabelaAgregado:
    id: int
    nome: str
    URL: str
    pesquisa: str
    assunto: str
    periodicidade: Periodicidade
    nivelTerritorial: NivelTerritorial
    variaveis: List[Variavel]
    classificacoes: List[Classificacao]

    @classmethod
    def from_json(cls: Type[T], data: dict) -> T:
        return cls(
            id=data["id"],
            nome=data["nome"],
            URL=data["URL"],
            pesquisa=data["pesquisa"],
            assunto=data["assunto"],
            periodicidade=Periodicidade(**data["periodicidade"]),
            nivelTerritorial=NivelTerritorial(**data["nivelTerritorial"]),
            variaveis=[Variavel(**v) for v in data["variaveis"]],
            classificacoes=[
                Classificacao(
                    id=c["id"],
                    nome=c["nome"],
                    sumarizacao=c["sumarizacao"],
                    categorias=[Categoria(**cat) for cat in c["categorias"]],
                )
                for c in data["classificacoes"]
            ],
        )
