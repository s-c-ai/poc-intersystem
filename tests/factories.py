# type: ignore
import factory
import factory.fuzzy

from poc_intersystem.models import ConsumeType, RawConsume, Regiao, User


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'test{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@test.com')
    password = factory.Faker('password')


class ConsumeFactory(factory.Factory):
    class Meta:
        model = RawConsume

    tipo = factory.fuzzy.FuzzyChoice(ConsumeType)
    regiao = factory.fuzzy.FuzzyChoice(Regiao)
    consumo = factory.Faker('pyint')
    ano = factory.fuzzy.FuzzyInteger(2018, 2023)
    mes = factory.fuzzy.FuzzyInteger(1, 12)
    month = factory.Faker('pystr')
    ipca = factory.Faker('pyfloat')
    dolar = factory.Faker('pyfloat')
    juros = factory.Faker('pyfloat')
    endividamento = factory.Faker('pyfloat')
    alcool = factory.Faker('pyint')
    pib_mensal = factory.Faker('pyfloat')
    utilizacao_industria = factory.Faker('pyfloat')
    aco_producao = factory.Faker('pyfloat')
    vendas_supermercado = factory.Faker('pyfloat')
    caged_construcao = factory.Faker('pyint')
    caged_energia = factory.Faker('pyint')
    caged_informacao = factory.Faker('pyint')
