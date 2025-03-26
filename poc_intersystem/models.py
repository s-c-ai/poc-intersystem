from enum import Enum

from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)


class ConsumeType(str, Enum):
    COMERCIAL = 'COMERCIAL'
    INDUSTRIAL = 'INDUSTRIAL'
    RESIDENCIAL = 'RESIDENCIAL'


class Regiao(str, Enum):
    CENTRO_OESTE = 'CENTRO-OESTE'
    NORTE = 'NORTE'
    NORDESTE = 'NORDESTE'
    SUL = 'SUL'
    SUDESTE = 'SUDESTE'


@table_registry.mapped_as_dataclass
class RawConsume:
    __tablename__ = 'raw_consumes'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    tipo: Mapped[ConsumeType]
    regiao: Mapped[Regiao]
    consumo: Mapped[int]
    ano: Mapped[int]
    mes: Mapped[int]
    month: Mapped[str]
    ipca: Mapped[float]
    dolar: Mapped[float]
    juros: Mapped[float]
    endividamento: Mapped[float]
    alcool: Mapped[int]
    pib_mensal: Mapped[float]
    utilizacao_industria: Mapped[float]
    aco_producao: Mapped[float]
    vendas_supermercado: Mapped[float]
    caged_construcao: Mapped[int]
    caged_energia: Mapped[int]
    caged_informacao: Mapped[int]
