"""
Sistema Especialista Médico - Interface Moderna (CustomTkinter)
Inspirada nos layouts SaaS HealthTech (Cards, Porcentagens e Painel Limpo).
"""

import os
import customtkinter as ctk
from tkinter import messagebox
from pyswip import Prolog


ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


INFO_DOENCAS = {
    "dengue": {
        "nome": "Dengue",
        "recomendacao": "Repouso e hidratação oral intensa.\nEvitar AAS e anti-inflamatórios.",
        "urgencia": "Alta ⚠️",
        "cor_tag": "#EF4444"
    },
    "covid19": {
        "nome": "COVID-19",
        "recomendacao": "Isolamento, monitorar saturação de O₂.\nAnalgésicos comuns se necessário.",
        "urgencia": "Média / Alta ⚠️",
        "cor_tag": "#F59E0B"
    },
    "gripe": {
        "nome": "Gripe (Influenza)",
        "recomendacao": "Analgésicos e antitérmicos.\nInjeção de líquidos e repouso.",
        "urgencia": "Leve 🟢",
        "cor_tag": "#10B981"
    },
    "resfriado": {
        "nome": "Resfriado Comum",
        "recomendacao": "Lavagem nasal com soro fisiológico.\nRepouso relativo.",
        "urgencia": "Leve 🟢",
        "cor_tag": "#10B981"
    },
    "sinusite": {
        "nome": "Sinusite",
        "recomendacao": "Irrigação nasal com soro 3x ao dia.\nCompressas meias no rosto.",
        "urgencia": "Moderada 🟡",
        "cor_tag": "#F59E0B"
    },
    "gastrite": {
        "nome": "Gastrite",
        "recomendacao": "Dieta leve, evitar condimentos e café.\nFracionar refeições.",
        "urgencia": "Moderada 🟡",
        "cor_tag": "#F59E0B"
    },
    "enxaqueca": {
        "nome": "Enxaqueca",
        "recomendacao": "Repouso em local escuro e silencioso.\nAnalgésico específico no início da dor.",
        "urgencia": "Moderada 🟡",
        "cor_tag": "#F59E0B"
    }
}

INFO_PADRAO = {
    "recomendacao": "Acompanhamento médico recomendado.\nManter hidratação.",
    "urgencia": "Avaliação 🔵",
    "cor_tag": "#3B82F6"
}


# =========================================================
# INTEGRACÃO PROLOG
# =========================================================
class MotorProlog:
    def __init__(self):
        self.prolog = Prolog()
        diretorio_python = os.path.dirname(os.path.abspath(__file__))
        diretorio_projeto = os.path.dirname(diretorio_python)
        caminho_prolog = os.path.join(diretorio_projeto, "prolog", "regras", "inferencia.pl")
        caminho_prolog = os.path.abspath(caminho_prolog).replace("\\", "/")

        if not os.path.isfile(caminho_prolog):
            raise FileNotFoundError(f"Arquivo Prolog não encontrado: {caminho_prolog}")

        self.prolog.consult(caminho_prolog)

    def obter_sintomas(self):
        consulta = "setof(S, D^sintoma(D, S), Lista)"
        res = list(self.prolog.query(consulta))
        if not res:
            return []
        return sorted([str(s) for s in res[0]["Lista"]])

    def diagnosticar(self, sintomas):
        if not sintomas:
            return []
        lista_str = "[" + ",".join(str(s) for s in sintomas) + "]"
        consulta = f"diagnosticar({lista_str}, R)"
        
        res = list(self.prolog.query(consulta))
        if not res:
            return []

        pares = res[0]["R"]
        ranking = []

        for par in pares:
            try:
                if hasattr(par, "args") and len(par.args) >= 2:
                    pontos = float(par.args[0])
                    doenca = str(par.args[1])
                else:
                    texto = str(par).strip()
                    if texto.startswith("-(") and texto.endswith(")"):
                        texto = texto[2:-1]
                    partes = texto.split(",", 1) if "," in texto else texto.split("-", 1)
                    pontos = float(partes[0].strip())
                    doenca = partes[1].strip()

                ranking.append((doenca, pontos))
            except Exception:
                continue

        return ranking


# =========================================================
# INTERFACE MODERNA (CUSTOMTKINTER)
# =========================================================
class AppModerno(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Symptom Checker & Differential Diagnosis")
        self.geometry("1100x700")
        self.minsize(980, 650)
        self.configure(fg_color="#F8FAFC")

        # Conexão Prolog
        try:
            self.motor = MotorProlog()
            self.sintomas_todos = self.motor.obter_sintomas()
        except Exception as e:
            messagebox.showerror("Erro Prolog", f"Falha ao carregar a base:\n{e}")
            self.destroy()
            return

        self.check_vars = {}
        self.sintomas_filtrados = list(self.sintomas_todos)

        self._construir_layout()

    def _construir_layout(self):
        # 1. BARRA SUPERIOR / HEADER (Estilo Imagem 5)
        self.header = ctk.CTkFrame(self, fg_color="#1E293B", corner_radius=0, height=60)
        self.header.pack(fill="x", side="top")

        lbl_titulo = ctk.CTkLabel(
            self.header, 
            text="🏥 Clinical Assistant & Differential Diagnosis", 
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#FFFFFF"
        )
        lbl_titulo.pack(side="left", padx=25, pady=15)

        # 2. CONTAINER PRINCIPAL (2 Colunas)
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(fill="both", expand=True, padx=20, pady=20)

        # ---------------------------------------------------------
        # COLUNA ESQUERDA: LISTA DE SINTOMAS E NAVEGAÇÃO
        # ---------------------------------------------------------
        self.col_esquerda = ctk.CTkFrame(self.container, fg_color="#FFFFFF", corner_radius=12, border_width=1, border_color="#E2E8F0")
        self.col_esquerda.place(relx=0.0, rely=0.0, relwidth=0.38, relheight=1.0)

        lbl_sint_head = ctk.CTkLabel(
            self.col_esquerda,
            text="Selected Symptoms",
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color="#1E293B"
        )
        lbl_sint_head.pack(anchor="w", padx=20, pady=(15, 5))

        # Campo de busca rápido
        self.entry_busca = ctk.CTkEntry(
            self.col_esquerda,
            placeholder_text="🔍 Search symptom...",
            fg_color="#F1F5F9",
            border_width=0,
            height=35
        )
        self.entry_busca.pack(fill="x", padx=15, pady=10)
        self.entry_busca.bind("<KeyRelease>", self._filtrar_sintomas)

        # Scroll de Checkboxes
        self.scroll_sintomas = ctk.CTkScrollableFrame(self.col_esquerda, fg_color="transparent")
        self.scroll_sintomas.pack(fill="both", expand=True, padx=10, pady=5)

        for s in self.sintomas_todos:
            var = ctk.BooleanVar(value=False)
            self.check_vars[s] = var

        self._renderizar_checkboxes()

        # Botão de Gerar Diagnóstico (Inspirado na Imagem 3)
        self.btn_gerar = ctk.CTkButton(
            self.col_esquerda,
            text="Generate Diagnosis 🚀",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            height=45,
            corner_radius=8,
            command=self._gerar_diagnostico
        )
        self.btn_gerar.pack(fill="x", padx=15, pady=15, side="bottom")

        # ---------------------------------------------------------
        # COLUNA DIREITA: CARDS DE DIAGNÓSTICO (Inspirado na Imagem 1)
        # ---------------------------------------------------------
        self.col_direita = ctk.CTkFrame(self.container, fg_color="transparent")
        self.col_direita.place(relx=0.40, rely=0.0, relwidth=0.60, relheight=1.0)

        lbl_diag_head = ctk.CTkLabel(
            self.col_direita,
            text="Possible Diagnoses",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#1E293B"
        )
        lbl_diag_head.pack(anchor="w", pady=(5, 15))

        # Scroll para os Cards de Resultado
        self.scroll_resultados = ctk.CTkScrollableFrame(self.col_direita, fg_color="transparent")
        self.scroll_resultados.pack(fill="both", expand=True)

        self._exibir_mensagem_inicial()

    # =========================================================
    # LÓGICA DE INTERFACE
    # =========================================================
    def _renderizar_checkboxes(self):
        for child in self.scroll_sintomas.winfo_children():
            child.destroy()

        for s in self.sintomas_filtrados:
            nome = s.replace("_", " ").capitalize()
            cb = ctk.CTkCheckBox(
                self.scroll_sintomas,
                text=nome,
                variable=self.check_vars[s],
                font=ctk.CTkFont(size=13),
                text_color="#334155",
                checkbox_width=20,
                checkbox_height=20,
                corner_radius=4,
                fg_color="#2563EB"
            )
            cb.pack(anchor="w", pady=6, padx=5)

    def _filtrar_sintomas(self, event=None):
        termo = self.entry_busca.get().lower().strip()
        if not termo:
            self.sintomas_filtrados = list(self.sintomas_todos)
        else:
            self.sintomas_filtrados = [
                s for s in self.sintomas_todos 
                if termo in s.replace("_", " ").lower()
            ]
        self._renderizar_checkboxes()

    def _exibir_mensagem_inicial(self):
        for child in self.scroll_resultados.winfo_children():
            child.destroy()

        lbl_vazio = ctk.CTkLabel(
            self.scroll_resultados,
            text="👈 Select symptoms on the left panel\nand click 'Generate Diagnosis'.",
            font=ctk.CTkFont(size=14, slant="italic"),
            text_color="#94A3B8"
        )
        lbl_vazio.pack(pady=50)

    def _gerar_diagnostico(self):
        sintomas_marcados = [s for s, var in self.check_vars.items() if var.get()]

        if not sintomas_marcados:
            messagebox.showwarning("Attention", "Please select at least one symptom.")
            return

        ranking = self.motor.diagnosticar(sintomas_marcados)

        # Limpa os cards anteriores
        for child in self.scroll_resultados.winfo_children():
            child.destroy()

        if not ranking:
            lbl_no_match = ctk.CTkLabel(
                self.scroll_resultados,
                text="No matching diagnosis found for the selected combination.",
                font=ctk.CTkFont(size=14),
                text_color="#EF4444"
            )
            lbl_no_match.pack(pady=30)
            return

        # RENDERIZA OS CARDS (Estilo similar ao da Imagem 1)
        for doenca, pct in ranking:
            info = INFO_DOENCAS.get(doenca, INFO_PADRAO)
            nome_doenca = info.get("nome", doenca.replace("_", " ").title())
            recomendacao = info.get("recomendacao", INFO_PADRAO["recomendacao"])
            urgencia = info.get("urgencia", INFO_PADRAO["urgencia"])
            cor_tag = info.get("cor_tag", INFO_PADRAO["cor_tag"])

            # Card Container
            card = ctk.CTkFrame(
                self.scroll_resultados, 
                fg_color="#FFFFFF", 
                corner_radius=12, 
                border_width=1, 
                border_color="#E2E8F0"
            )
            card.pack(fill="x", pady=8, padx=5)

            # Cabecalho do Card (Nome + Porcentagem)
            header_card = ctk.CTkFrame(card, fg_color="transparent")
            header_card.pack(fill="x", padx=15, pady=(12, 5))

            lbl_nome = ctk.CTkLabel(
                header_card,
                text=f"{nome_doenca} ({pct:.0f}%)",
                font=ctk.CTkFont(size=15, weight="bold"),
                text_color="#0F172A"
            )
            lbl_nome.pack(side="left")

            lbl_urg = ctk.CTkLabel(
                header_card,
                text=urgencia,
                font=ctk.CTkFont(size=11, weight="bold"),
                text_color=cor_tag,
                fg_color="#F1F5F9",
                corner_radius=6,
                padx=8,
                pady=2
            )
            lbl_urg.pack(side="right")

            # Divider
            divider = ctk.CTkFrame(card, fg_color="#F1F5F9", height=1)
            divider.pack(fill="x", padx=15, pady=5)

            # Corpo do Card (Recomendações/Medicação)
            lbl_rec_title = ctk.CTkLabel(
                card,
                text="Suggested Care / Next Steps:",
                font=ctk.CTkFont(size=11, weight="bold"),
                text_color="#64748B"
            )
            lbl_rec_title.pack(anchor="w", padx=15, pady=(2, 0))

            lbl_rec_desc = ctk.CTkLabel(
                card,
                text=recomendacao,
                font=ctk.CTkFont(size=12),
                text_color="#334155",
                justify="left"
            )
            lbl_rec_desc.pack(anchor="w", padx=15, pady=(0, 12))


if __name__ == "__main__":
    app = AppModerno()
    app.mainloop()