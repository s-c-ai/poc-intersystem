import pandera as pa
from pydantic import BaseModel


class EnergyConsumeRaw(pa.DataFrameModel):
    tipo: str = pa.Field(isin=['COMERCIAL', 'INDUSTRIAL', 'RESIDENCIAL'])
    regiao: str = pa.Field(
        isin=['CENTRO-OESTE', 'NORTE', 'NORDESTE', 'SUL', 'SUDESTE']
    )
    consumo: int
    ano: int
    mes: int
    month: str
    ipca: float
    dolar: float
    juros: float
    endividamento: float
    alcool: int
    pib_mensal: float
    utilizacao_industria: float
    aco_producao: float
    vendas_supermercado: float
    caged_construcao: int
    caged_energia: int
    caged_informacao: int


class ConsumePublic(BaseModel):
    id: int


class ConsumeList(BaseModel):
    ids: list[ConsumePublic]
