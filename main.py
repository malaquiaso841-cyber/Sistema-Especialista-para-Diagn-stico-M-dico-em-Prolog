"""
Sistema de Diagnóstico por Sintomas - Integração Python + Prolog
----------------------------------------------------------------

Estrutura esperada:

SEU_PROJETO/
│
├── python/
│   ├── main.py
│   └── interface.py
│
└── prolog/
    ├── doencas.pl
    └── inferencia.pl

Requisitos:
    pip install pyswip

Também é necessário ter o SWI-Prolog instalado no Windows.
"""

import os
from pyswip import Prolog

AVISO_EDUCACIONAL = (
    "\n[AVISO] Este sistema tem fins EDUCACIONAIS e não substitui uma\n"
    "consulta médica. Os resultados são apenas sugestões baseadas em\n"
    "correspondência de sintomas, não um diagnóstico real.\n"
)


class DiagnosticoApp:
    def __init__(self, arquivo_prolog=None):
        """
        Inicializa o Prolog e carrega o arquivo inferencia.pl.
        """
        self.prolog = Prolog()

        # Diretório onde está este arquivo Python (main.py está na raiz do projeto)
        diretorio_projeto = os.path.dirname(os.path.abspath(__file__))

        # Pasta prolog
        diretorio_prolog = os.path.join(diretorio_projeto, "prolog")

        # Caso nenhum arquivo seja informado, utiliza automaticamente inferencia.pl
        if arquivo_prolog is None:
            caminho_prolog = os.path.join(diretorio_prolog, "regras", "inferencia.pl")
        else:
            caminho_prolog = arquivo_prolog

        # Converte para caminho absoluto e ajusta barras para compatibilidade com o Prolog
        caminho_prolog = os.path.abspath(caminho_prolog).replace("\\", "/")

        # Verifica se inferencia.pl existe
        if not os.path.isfile(caminho_prolog):
            raise FileNotFoundError(
                "Arquivo inferencia.pl não encontrado.\n\n"
                f"Caminho procurado: {caminho_prolog}"
            )

        # Carrega o arquivo Prolog
        self.prolog.consult(caminho_prolog)

        # Carrega os sintomas disponíveis
        self.sintomas_disponiveis = self._carregar_sintomas()

    # =====================================================
    # INTEGRAÇÃO COM PROLOG
    # =====================================================

    def _carregar_sintomas(self):
        """
        Busca no Prolog todos os sintomas distintos cadastrados.
        """
        consulta = "setof(S, D^sintoma(D, S), Lista)"

        resultados = list(self.prolog.query(consulta))

        if not resultados:
            return []

        lista = resultados[0]["Lista"]

        return sorted(str(sintoma) for sintoma in lista)

    def enviar_sintomas(self, sintomas):
        if not sintomas:
            return []

        # Monta a lista no formato aceito pelo Prolog
        lista_prolog = "[" + ",".join(str(sintoma) for sintoma in sintomas) + "]"
        consulta = f"diagnosticar({lista_prolog}, R)"

        print("\n" + "=" * 60)
        print("DEBUG - TESTE DA INTEGRAÇÃO PYTHON + PROLOG")
        print("=" * 60)
        print("\nDEBUG - Consulta:", consulta)

        try:
            resultados = list(self.prolog.query(consulta))
        except Exception as erro:
            print("\nERRO AO CONSULTAR O PROLOG:", erro)
            return []

        if not resultados:
            print("\nDEBUG - O Prolog não retornou nenhuma solução.")
            return []

        # =====================================================
        # CONVERSÃO DOS RESULTADOS TRATADA
        # =====================================================
        pares = resultados[0]["R"]
        print("\nDEBUG - Pares recebidos do Prolog:", pares)

        ranking = []

        for par in pares:
            try:
                # Caso 1: Objeto PySwip com atributos de argumentos (.args)
                if hasattr(par, "args") and len(par.args) >= 2:
                    pontuacao = float(par.args[0])
                    doenca = str(par.args[1])

                # Caso 2: String do Prolog, ex: '-(20.0, rinite_alergica)'
                else:
                    texto = str(par).strip()

                    # Remove ' -(' do início e ')' do fim se existirem
                    if texto.startswith("-(") and texto.endswith(")"):
                        texto = texto[2:-1]

                    # Separa por vírgula (ex: '20.0, rinite_alergica')
                    if "," in texto:
                        partes = texto.split(",", 1)
                    else:
                        partes = texto.split("-", 1)

                    pontuacao = float(partes[0].strip())
                    doenca = partes[1].strip()

                ranking.append((doenca, pontuacao))

            except Exception as erro:
                print(f"\nDEBUG - Erro ao interpretar o par '{par}': {erro}")
                continue

        print("\nDEBUG - Ranking final processado:", ranking)
        print("=" * 60)

        return ranking

    # =====================================================
    # INTERFACE DE TERMINAL
    # =====================================================

    def exibir_sintomas(self):
        print("\nSintomas disponíveis:")
        for i, sintoma in enumerate(self.sintomas_disponiveis, start=1):
            print(f"  {i:2d}. {sintoma}")

    def selecionar_sintomas(self):
        """
        Permite ao usuário escolher vários sintomas
        pelo número, separados por vírgula.
        """
        while True:
            self.exibir_sintomas()

            entrada = input(
                "\nDigite os números dos sintomas que você sente, "
                "separados por vírgula (ex: 1,4,10): "
            ).strip()

            if not entrada:
                print("Entrada vazia. Tente novamente.\n")
                continue

            partes = [p.strip() for p in entrada.split(",") if p.strip()]

            try:
                indices = [int(p) for p in partes]
            except ValueError:
                print("Entrada inválida. Use apenas números separados por vírgula.\n")
                continue

            invalidos = [
                i for i in indices
                if i < 1 or i > len(self.sintomas_disponiveis)
            ]

            if invalidos:
                print(f"Números fora do intervalo válido: {invalidos}\n")
                continue

            if not indices:
                print("Você precisa selecionar pelo menos um sintoma.\n")
                continue

            # Remove duplicados mantendo a ordem
            indices_unicos = list(dict.fromkeys(indices))

            sintomas_escolhidos = [
                self.sintomas_disponiveis[i - 1] for i in indices_unicos
            ]

            return sintomas_escolhidos

    def exibir_ranking(self, ranking):
        print("\n" + "=" * 50)
        print("RANKING DE POSSÍVEIS DOENÇAS")
        print("=" * 50)

        if not ranking:
            print("Nenhuma doença encontrada com os sintomas informados.")
        else:
            for posicao, (doenca, pontuacao) in enumerate(ranking, start=1):
                nome_formatado = doenca.replace("_", " ").title()
                print(
                    f"{posicao}. {nome_formatado:<25} "
                    f"- {pontuacao:5.1f}% de compatibilidade"
                )

        print(AVISO_EDUCACIONAL)

    # =====================================================
    # MENU
    # =====================================================

    def executar_menu(self):
        print("=" * 50)
        print("SISTEMA DE DIAGNÓSTICO POR SINTOMAS (Prolog + Python)")
        print("=" * 50)
        print(AVISO_EDUCACIONAL)

        while True:
            print("\nMENU")
            print("1. Selecionar sintomas e ver diagnóstico")
            print("2. Sair")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                sintomas = self.selecionar_sintomas()
                print("\nSintomas selecionados: " + ", ".join(sintomas))

                try:
                    ranking = self.enviar_sintomas(sintomas)
                    self.exibir_ranking(ranking)
                except Exception as erro:
                    print("\nErro ao consultar o Prolog:")
                    print(erro)

            elif opcao == "2":
                print("Encerrando o sistema. Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.")


# =========================================================
# EXECUÇÃO
# =========================================================

def main():
    try:
        app = DiagnosticoApp()
        app.executar_menu()
    except Exception as erro:
        print("\nERRO AO INICIAR O SISTEMA:")
        print(erro)


if __name__ == "__main__":
    main()