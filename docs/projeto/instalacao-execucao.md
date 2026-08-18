# Instalação e Execução

## Requisitos

Para executar o projeto, é necessário instalar:

- Python 3;
- SWI-Prolog;
- Biblioteca PySwip;
- Biblioteca CustomTkinter.

## Instalação das dependências

Abra o terminal na pasta principal do projeto e execute:

```powershell
py -m pip install pyswip customtkinter
```

Caso o projeto possua todas as dependências em `requirements.txt`, também é possível executar:

```powershell
py -m pip install -r requirements.txt
```

O SWI-Prolog deve ser instalado separadamente. Para verificar se ele está disponível, execute:

```powershell
swipl --version
```

## Estrutura necessária

Os arquivos principais devem permanecer nesta organização:

```text
projeto/
├── main.py
├── python/
│   └── interface.py
└── prolog/
    ├── base_conhecimento/
    │   └── doencas.pl
    └── regras/
        └── inferencia.pl
```

Essa estrutura é necessária para que o Python localize e carregue os arquivos Prolog.

## Executar pelo terminal

Na pasta principal do projeto, execute:

```powershell
py main.py
```

O sistema exibirá os sintomas disponíveis e permitirá que o usuário faça a seleção digitando os números correspondentes.

## Executar a interface gráfica

Na pasta principal do projeto, execute:

```powershell
py python\interface.py
```

A interface gráfica será aberta e permitirá pesquisar, selecionar sintomas e gerar o ranking de possíveis doenças.

## Possíveis erros

Se aparecer um erro informando que `inferencia.pl` não foi encontrado, verifique se as pastas estão organizadas corretamente.

Se aparecer um erro relacionado ao `pyswip` ou `libswipl`, verifique se o SWI-Prolog está instalado e disponível no `PATH` do Windows.

> O sistema possui finalidade educacional e não substitui uma consulta ou um diagnóstico médico.