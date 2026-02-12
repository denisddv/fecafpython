import csv
from datetime import date
from typing import List, Dict


def gerar_parcelas_aluguel(valor_mensal: float, meses: int = 12) -> List[Dict[str, str]]:
    """
    Gera uma lista de parcelas mensais (12 meses).
    Observação: o enunciado pede 'arquivo .csv com as 12 parcelas do orçamento'.
    Aqui usamos 12 linhas, uma por mês.
    """
    hoje = date.today()
    parcelas = []
    for i in range(1, meses + 1):
        parcelas.append({
            "parcela": str(i),
            "mes_referencia": f"{hoje.year}-{str(hoje.month).zfill(2)}",
            "valor_aluguel": f"{valor_mensal:.2f}"
        })
        # incrementa mês (simples)
        if hoje.month == 12:
            hoje = date(hoje.year + 1, 1, 1)
        else:
            hoje = date(hoje.year, hoje.month + 1, 1)

    return parcelas


def exportar_csv(parcelas: List[Dict[str, str]], caminho: str) -> None:
    if not parcelas:
        raise ValueError("Lista de parcelas vazia.")

    colunas = list(parcelas[0].keys())
    with open(caminho, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=colunas, delimiter=";")
        writer.writeheader()
        writer.writerows(parcelas)
