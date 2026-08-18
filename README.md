# Sistema Especialista para Diagnóstico Médico em Prolog

## Informações acadêmicas

- **Instituição:** Universidade Federal do Cariri (UFCA)
- **Curso:** [Engenharia de software]
- **Disciplina:** [Paradigmas de prgramação]
- **Professor:** [Rafael Will Macedo de Araújo]
- **Integrantes:**
  - [Malaquias de oliveira do nascimento]
  - [Dorian Dayvid Gomes Feitosa]
  - [José Luiz de Lima Mendes]
  - [Pedro Igor Medeiros Cunha]
- **Período:** [Semestre 3 | ano 2026]

---

## Descrição do projeto

Este projeto apresenta um sistema especialista educacional desenvolvido com **Python** e **Prolog**.

O sistema permite que o usuário selecione sintomas e receba um ranking de possíveis doenças baseado na compatibilidade entre os sintomas informados e os dados armazenados na base de conhecimento.

O Python é responsável pela interação com o usuário e pela apresentação dos resultados. O Prolog armazena as doenças, os sintomas e as regras utilizadas no processo de inferência.

O projeto disponibiliza duas formas de utilização:

- Interface de terminal;
- Interface gráfica desenvolvida com CustomTkinter.

> **Aviso:** o sistema possui finalidade exclusivamente educacional. Os resultados não representam um diagnóstico médico e não substituem uma consulta com um profissional da saúde.

---

## Objetivos

### Objetivo geral

Desenvolver um sistema especialista utilizando Prolog para representar conhecimentos e aplicar regras de inferência no domínio de diagnóstico por sintomas.

### Objetivos específicos

- Estudar os fundamentos da programação lógica;
- Representar doenças e sintomas por meio de fatos Prolog;
- Criar regras para calcular compatibilidades;
- Integrar Python e Prolog utilizando PySwip;
- Desenvolver interfaces para interação com o usuário;
- Organizar a documentação técnica em Markdown;
- Demonstrar o funcionamento de um sistema especialista.

---

## Funcionalidades

O sistema possui as seguintes funcionalidades:

- Listagem dos sintomas cadastrados;
- Seleção de múltiplos sintomas;
- Pesquisa de sintomas na interface gráfica;
- Validação da entrada do usuário;
- Verificação de sintomas obrigatórios;
- Cálculo ponderado de compatibilidade;
- Ordenação das doenças por porcentagem;
- Exibição de um ranking de possíveis doenças;
- Recomendações educacionais na interface gráfica;
- Execução pelo terminal;
- Execução por interface gráfica.

---

## Tecnologias utilizadas

- **Python 3:** controle da aplicação e tratamento dos resultados;
- **Prolog:** representação da base de conhecimento e das regras;
- **SWI-Prolog:** execução do código Prolog;
- **PySwip:** integração entre Python e SWI-Prolog;
- **CustomTkinter:** construção da interface gráfica;
- **Tkinter:** exibição de mensagens da interface;
- **Markdown:** produção da documentação;
- **Git e GitHub:** versionamento e armazenamento do projeto.

---

## Arquitetura

O sistema está organizado em três partes principais:

1. **Interface:** recebe os sintomas e apresenta os resultados;
2. **Integração:** realiza a comunicação entre Python e Prolog por meio do PySwip;
3. **Sistema especialista:** armazena o conhecimento e executa as regras de inferência.

```mermaid
flowchart LR
    A["Usuário"] --> B["Interface Python"]
    B --> C["PySwip"]
    C --> D["Regras Prolog"]
    D --> E["Base de conhecimento"]
    E --> D
    D --> C
    C --> B
    B --> A
```

---

## Estrutura do projeto

```text
Sistema-Especialista-para-Diagnostico-Medico-em-Prolog/
├── docs/
│   ├── analise-critica/
│   │   └── analise.md
│   ├── pesquisa/
│   │   ├── biografia.md
│   │   ├── contextualizacao-historica.md
│   │   ├── fundamentos-prolog.md
│   │   ├── sistemas-especialistas.md
│   │   └── referencias.md
│   └── projeto/
│       ├── arquitetura.md
│       ├── funcionamento.md
│       ├── instalacao-execucao.md
│       └── integracao-python-prolog.md
├── prolog/
│   ├── base_conhecimento/
│   │   └── doencas.pl
│   └── regras/
│       ├
│       └── inferencia.pl
├── python/
│   ├── __init__.py
│   └── interface.py
├── tests/
│   └── testes.md
├── main.py
├── requirements.txt
├── LICENSE
├── README.md
└── .gitignore
```

---

## Funcionamento

O funcionamento do sistema segue estas etapas:

1. A aplicação Python é iniciada;
2. O PySwip inicializa o SWI-Prolog;
3. O arquivo `inferencia.pl` é carregado;
4. O Prolog carrega a base `doencas.pl`;
5. Os sintomas cadastrados são apresentados ao usuário;
6. O usuário seleciona um ou mais sintomas;
7. O Python envia a lista ao Prolog;
8. O Prolog verifica as doenças compatíveis;
9. Os pesos dos sintomas correspondentes são somados;
10. As porcentagens são calculadas;
11. Os resultados são ordenados;
12. A interface apresenta o ranking ao usuário.

A consulta principal possui o seguinte formato:

```prolog
diagnosticar([febre, tosse, dor_cabeca], Resultado).
```

---

## Base de conhecimento

A base de conhecimento está localizada em:

```text
prolog/base_conhecimento/doencas.pl
```

As doenças são representadas por fatos:

```prolog
doenca(dengue).
doenca(gripe).
doenca(covid19).
```

Os sintomas são cadastrados com a seguinte estrutura:

```prolog
sintoma(Doenca, Sintoma, Peso, Obrigatorio).
```

Exemplo:

```prolog
sintoma(dengue, febre, 4, sim).
sintoma(dengue, dor_muscular, 3, nao).
sintoma(dengue, dor_atras_olhos, 5, nao).
```

O peso indica a importância do sintoma. Quando o último valor é `sim`, o sintoma é obrigatório para que a doença participe do ranking.

---

## Cálculo da compatibilidade

A porcentagem de compatibilidade é calculada por meio da fórmula:

```text
Compatibilidade = (peso obtido ÷ peso total da doença) × 100
```

O peso obtido corresponde à soma dos pesos dos sintomas selecionados que estão relacionados à doença.

O resultado representa apenas uma correspondência matemática entre os sintomas e a base cadastrada. Ele não representa a probabilidade clínica real de uma doença.

---

## Requisitos

Antes de executar o projeto, é necessário instalar:

- Python 3;
- SWI-Prolog;
- PySwip;
- CustomTkinter.

Para verificar as instalações do Python e do SWI-Prolog, execute:

```powershell
py --version
swipl --version
```

---

## Instalação

### 1. Clonar o repositório

```powershell
git clone [https://github.com/malaquiaso841-cyber/Sistema-Especialista-para-Diagn-stico-M-dico-em-Prolog.git]
```

Entre na pasta:

```powershell
cd Sistema-Especialista-para-Diagnostico-Medico-em-Prolog
```

### 2. Instalar as dependências

```powershell
py -m pip install -r requirements.txt
```

Também é possível instalar as dependências diretamente:

```powershell
py -m pip install pyswip customtkinter
```

### 3. Verificar o SWI-Prolog

```powershell
swipl --version
```

O comando deve apresentar a versão instalada.

---

## Execução

Os comandos devem ser executados na pasta principal do projeto.

### Interface de terminal

```powershell
py main.py
```

A aplicação mostrará um menu com os sintomas cadastrados.

### Interface gráfica

```powershell
py python\interface.py
```

A aplicação abrirá uma janela para pesquisar e selecionar sintomas.

---

## Testes

Os testes e resultados observados durante o desenvolvimento estão documentados em:

```text
tests/testes.md
```

Os principais pontos testados incluem:

- Carregamento da base Prolog;
- Consulta dos sintomas cadastrados;
- Seleção de um ou vários sintomas;
- Validação de sintomas obrigatórios;
- Cálculo das porcentagens;
- Ordenação do ranking;
- Comunicação entre Python e Prolog;
- Execução da interface de terminal;
- Execução da interface gráfica.

---

## Documentação

A documentação completa do projeto está disponível nos seguintes arquivos:

### Pesquisa

- [Contextualização histórica](docs/pesquisa/contextualizacao-historica.md);
- [Fundamentos de Prolog](docs/pesquisa/fundamentos-prolog.md);
- [Sistemas especialistas](docs/pesquisa/sistemas-especialistas.md);
- [Referências](docs/pesquisa/referencias.md).

### Projeto

### Pesquisa

- [Conceitos e paradigmas](docs/pesquisa/conceitos-paradigma.md);
- [Contextualização histórica](docs/pesquisa/contextualizacao-historica.md);
- [Pesquisa bibliográfica](docs/pesquisa/pesquisa-bibliografica.md);
- [Sistemas especialistas](docs/pesquisa/sistemas-especialistas.md);
- [Referências bibliográficas](docs/pesquisa/referencias.md).

### Análise

- [Análise crítica](docs/analise-critica/analise.md).

---

## Limitações

O sistema possui algumas limitações:

- Trabalha somente com doenças e sintomas previamente cadastrados;
- Não considera idade, histórico clínico ou duração dos sintomas;
- Não utiliza exames laboratoriais;
- Não considera a possibilidade de múltiplas doenças simultâneas;
- As recomendações são fixas e educacionais;
- A porcentagem calculada não representa uma probabilidade médica;
- O sistema não substitui a avaliação de um profissional.

---

## Possíveis melhorias

Como trabalhos futuros, podem ser implementadas as seguintes melhorias:

- Ampliação da base de doenças;
- Cadastro de novos sintomas;
- Inclusão de perguntas adicionais;
- Histórico de consultas;
- Persistência em banco de dados;
- Explicação detalhada de cada resultado;
- Centralização da integração em um único módulo Python;
- Desenvolvimento de uma interface web;
- Criação de testes automatizados.

---

## Referências

SWI-PROLOG. **SWI-Prolog documentation**. Disponível em: <https://www.swi-prolog.org/pldoc/>. 

PYSWIP. **PySwip documentation**. Disponível em: <https://pyswip.readthedocs.io/>. 

CUSTOMTKINTER. **CustomTkinter documentation**. Disponível em: <https://customtkinter.tomschimansky.com/documentation/

PYTHON SOFTWARE FOUNDATION. **Python documentation**. Disponível em: <https://docs.python.org/3/>. 


As referências utilizadas na pesquisa e no desenvolvimento estão disponíveis em [Referências da pesquisa](docs/pesquisa/referencias.md).


---

## Licença

Este projeto foi desenvolvido para fins acadêmicos na Universidade Federal do Cariri.

Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.