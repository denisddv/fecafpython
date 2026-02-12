from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class Contrato:
    valor_total: float = 2000.0
    max_parcelas: int = 5

    def calcular_parcelas(self, qtd_parcelas: int) -> float:
        if qtd_parcelas < 1 or qtd_parcelas > self.max_parcelas:
            raise ValueError(f"Parcelas inválidas: escolha entre 1 e {self.max_parcelas}.")
        return self.valor_total / qtd_parcelas


@dataclass
class Imovel:
    """Classe base. Cada tipo de imóvel implementa seu cálculo."""
    tipo: str

    def calcular_aluguel(self) -> float:
        raise NotImplementedError


@dataclass
class Apartamento(Imovel):
    quartos: int = 1
    garagem: bool = False
    possui_criancas: bool = True

    BASE_1Q: float = 700.0

    def calcular_aluguel(self) -> float:
        valor = self.BASE_1Q
        if self.quartos == 2:
            valor += 200.0  # acréscimo 2 quartos
        if self.garagem:
            valor += 300.0  # garagem apto/casa
        # desconto 5% se NÃO possui crianças
        if not self.possui_criancas:
            valor *= 0.95
        return valor


@dataclass
class Casa(Imovel):
    quartos: int = 1
    garagem: bool = False

    BASE_1Q: float = 900.0

    def calcular_aluguel(self) -> float:
        valor = self.BASE_1Q
        if self.quartos == 2:
            valor += 250.0  # acréscimo 2 quartos
        if self.garagem:
            valor += 300.0  # garagem apto/casa
        return valor


@dataclass
class Estudio(Imovel):
    vagas: int = 0

    BASE: float = 1200.0

    def calcular_aluguel(self) -> float:
        valor = self.BASE
        # Regras:
        # - se quiser vagas: 2 vagas custam 250
        # - vagas extras custam 60 cada (acima de 2)
        if self.vagas <= 0:
            return valor

        if self.vagas <= 2:
            valor += 250.0
        else:
            extras = self.vagas - 2
            valor += 250.0 + (extras * 60.0)
        return valor
