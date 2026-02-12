from models import Contrato, Apartamento, Casa, Estudio
from services import gerar_parcelas_aluguel, exportar_csv


def perguntar_int(msg: str, validos: set[int] | None = None) -> int:
    while True:
        try:
            v = int(input(msg).strip())
            if validos is not None and v not in validos:
                print(f"Valor inválido. Opções: {sorted(validos)}")
                continue
            return v
        except ValueError:
            print("Digite um número válido.")


def perguntar_bool(msg: str) -> bool:
    while True:
        v = input(msg + " (s/n): ").strip().lower()
        if v in ("s", "sim"):
            return True
        if v in ("n", "nao", "não"):
            return False
        print("Responda com 's' ou 'n'.")


def main():
    print("=== ORÇAMENTO DE ALUGUEL (R.M Imobiliária) ===")
    print("1) Apartamento")
    print("2) Casa")
    print("3) Estúdio")

    opcao = perguntar_int("Escolha o tipo de imóvel (1-3): ", {1, 2, 3})

    imovel = None

    if opcao == 1:
        quartos = perguntar_int("Quantidade de quartos (1 ou 2): ", {1, 2})
        garagem = perguntar_bool("Deseja incluir vaga de garagem?")
        possui_criancas = perguntar_bool("A pessoa possui crianças?")
        imovel = Apartamento(tipo="Apartamento", quartos=quartos, garagem=garagem, possui_criancas=possui_criancas)

    elif opcao == 2:
        quartos = perguntar_int("Quantidade de quartos (1 ou 2): ", {1, 2})
        garagem = perguntar_bool("Deseja incluir vaga de garagem?")
        imovel = Casa(tipo="Casa", quartos=quartos, garagem=garagem)

    else:
        vagas = perguntar_int("Quantidade de vagas de estacionamento (0 ou mais): ")
        if vagas < 0:
            vagas = 0
        imovel = Estudio(tipo="Estúdio", vagas=vagas)

    aluguel_mensal = imovel.calcular_aluguel()

    print("\n--- RESULTADO DO ORÇAMENTO ---")
    print(f"Tipo: {imovel.tipo}")
    print(f"Aluguel mensal orçado: R$ {aluguel_mensal:.2f}")

    # Contrato
    contrato = Contrato(valor_total=2000.0, max_parcelas=5)
    qtd_parcelas = perguntar_int("Em quantas vezes deseja parcelar o contrato? (1 a 5): ", {1, 2, 3, 4, 5})
    valor_parcela_contrato = contrato.calcular_parcelas(qtd_parcelas)

    print(f"Contrato imobiliário: R$ {contrato.valor_total:.2f}")
    print(f"Parcelamento do contrato: {qtd_parcelas}x de R$ {valor_parcela_contrato:.2f}")

    # CSV 12 parcelas do orçamento (aluguel mensal)
    gerar = perguntar_bool("Deseja gerar o CSV com as 12 parcelas do orçamento?")
    if gerar:
        parcelas = gerar_parcelas_aluguel(aluguel_mensal, meses=12)
        caminho = "parcelas_orcamento.csv"
        exportar_csv(parcelas, caminho)
        print(f"CSV gerado com sucesso: {caminho}")

    print("\nFim.")


if __name__ == "__main__":
    main()
