# Prolog

## 1. Introdução

**PROLOG** (*PROgramming in LOGic*) é uma linguagem de programação em lógica baseada em um subconjunto da lógica de primeira ordem, denominado **cláusulas de Horn**. As cláusulas de Horn possuem um algoritmo de busca eficiente que permite uma performance competitiva.

Pode-se dizer que um programa PROLOG é uma base de dados composta de **regras e fatos**. Como tal, a linguagem é naturalmente **declarativa**: o desenvolvedor informa ao sistema como especificar o problema e o sistema, por sua vez, utiliza um algoritmo de busca para responder às questões.

Embora seja uma linguagem declarativa, algumas características não lógicas foram adicionadas ao PROLOG, tais como:

* Controle de fluxo;
* Entrada e saída;
* Metaprogramação.

### Principais características do PROLOG

* É uma linguagem orientada ao processamento de símbolos, os chamados **termos**.
* Implementa uma lógica como linguagem de programação.
* Apresenta uma semântica declarativa inerente a uma lógica.
* Permite a definição de programas reversíveis, isto é, programas que não fazem distinção entre os argumentos de entrada e os de saída.
* Permite a obtenção de respostas alternativas.
* Suporta naturalmente código recursivo e iterativo para a descrição de processos e problemas, dispensando mecanismos tradicionais de controle, tais como comandos de repetição.
* Permite associar o processo de especificação ao processo de codificação de programas.
* Representa programas e dados através do mesmo formalismo.

---

## 2. História e Aplicações

A história do **Prolog** remonta à década de 1970, com o trabalho de **Alain Colmerauer** e **Philippe Roussel**, na Universidade de Aix-Marseille, na França.

Desde então, a linguagem evoluiu e se espalhou pelo mundo, ganhando destaque em diversas aplicações. A principal utilização da linguagem PROLOG reside no domínio da **programação simbólica**, sendo especialmente adequada à solução de problemas envolvendo relações entre objetos.

O Prolog surgiu de um projeto que tinha como objetivo inicial não criar uma linguagem de programação, mas sim **processar linguagens naturais**, tendo o francês como foco inicial. O projeto resultou em uma versão preliminar do Prolog no final de **1971** e em uma versão mais definitiva no final de **1972**.

### Principais aplicações

Entre suas aplicações, podemos destacar:

* **Inteligência Artificial:** sistemas especialistas e raciocínio automatizado.
* **Processamento de Linguagem Natural (PLN):** análise sintática e geração de texto.
* **Bancos de dados dedutivos:** consultas complexas e inferência de conhecimento.
* **Verificação de modelos e sistemas:** análise de correção e detecção de erros.
* **Resolução de problemas de otimização:** planejamento e alocação de recursos.

---

## 3. Funcionamento do Paradigma

Para entender o Prolog e outras linguagens lógicas, é essencial dominar alguns conceitos básicos.

### 3.1 Fatos

Os **fatos** são declarações que afirmam algo sobre o mundo.

Por exemplo:

```prolog
gato(tom).
```

Nesse caso, o fato afirma que **Tom é um gato**.

### 3.2 Regras

As **regras** definem relações entre fatos.

Por exemplo:

```prolog
animal(X) :- gato(X).
```

Essa regra pode ser interpretada como:

> Se `X` é um gato, então `X` é um animal.

### 3.3 Consultas

As **consultas** são perguntas feitas ao sistema Prolog para verificar se determinada informação é verdadeira ou para encontrar valores que satisfaçam uma determinada condição.

Por exemplo:

```prolog
?- animal(tom).
```

A consulta busca determinar se **Tom é um animal**.

---

## 4. Sintaxe do Prolog

A sintaxe do Prolog é simples e elegante. Um programa Prolog consiste em uma série de **cláusulas**, que podem ser fatos ou regras.

Em Prolog, existe apenas um tipo básico chamado **termo**, que engloba todas as construções sintáticas da linguagem.

Um termo pode ser:

* Uma constante;
* Uma variável;
* Uma estrutura.

### 4.1 Constantes

As constantes podem ser **átomos** ou **números**.

Um **átomo** indica um objeto ou uma relação. Nomes de objetos como `maria`, `livro` etc. são átomos.

Os nomes de átomos normalmente começam com **letra minúscula**. Os nomes de predicados também são atômicos.

Os grupos de caracteres `?-` (usado em perguntas) e `:-` (usado em regras) também fazem parte da sintaxe do Prolog.

Em relação aos números, o Prolog permite:

* Inteiros positivos;
* Inteiros negativos;
* Números em ponto flutuante utilizando ponto decimal;
* Opcionalmente, números utilizando expoente de dez.

**Exemplos:**

```prolog
maria
livro
42
-10
3.14
```

### 4.2 Variáveis

Sintaticamente, as variáveis possuem nomes cujo primeiro caractere é uma **letra maiúscula** ou o sinal de sublinhado (`_`).

Exemplos:

```prolog
X
Pessoa
Livro
```

As variáveis cujo nome é composto pelo caractere `_` são chamadas de **variáveis anônimas**.

Variáveis com o mesmo nome aparecendo em uma mesma cláusula representam a mesma variável. Dessa forma, se uma variável recebe um valor, esse valor passa imediatamente para as outras ocorrências da mesma variável.

As variáveis anônimas possuem um comportamento diferente: cada ocorrência de `_` representa uma variável diferente, mesmo dentro de uma mesma cláusula.

Além disso, quando variáveis anônimas são utilizadas em uma pergunta, seus valores não são impressos nas respostas.

As variáveis anônimas são utilizadas quando desejamos que uma variável possa **unificar com qualquer termo**, mas não temos interesse em saber qual valor será atribuído a ela.

**Exemplo:**

```prolog
animal(_, gato).
```

Nesse caso, o primeiro argumento pode ser qualquer termo, mas o valor específico não é relevante para a regra ou consulta.

### 4.3 Estruturas

As **estruturas** são termos mais complexos, formados por um **funtor** seguido de componentes separados por vírgulas e colocados entre parênteses.

Por exemplo, para representar um livro com seu título e autor, podemos utilizar a seguinte estrutura:

```prolog
livro(incidente_em_antares, verissimo).
```

Nesse exemplo:

* `livro` é o **funtor**;
* `incidente_em_antares` representa o título;
* `verissimo` representa o autor.

As estruturas permitem representar informações mais complexas por meio da combinação de diferentes termos.


## Referências:

https://helloup.com.br/programao-lgica-prolog/

COLMERAUER, Alain; ROUSSEL, Philippe. The birth of Prolog. In: History of programming languages---II. 1996. p. 331-367. https://dl.acm.org/doi/epdf/10.1145/234286.1057820

Souza Oliveira, George & Faustino, Anderson. (2013). Prolog: A Linguagem, A Máquina Abstrata de Warren e Implementações. Revista de Informática Teórica e Aplicada. 20. 214. 10.22456/2175-2745.36756. https://www.researchgate.net/publication/332587152_Prolog_A_Linguagem_A_Maquina_Abstrata_de_Warren_e_Implementacoes

# Análise Crítica: Maturidade, Ecossistema e Perspectivas do Prolog

## Maturidade
Prolog existe desde 1972 e tem padrão ISO ([ISO/IEC 13211](https://www.iso.org/standard/21413.html)). É uma linguagem tecnicamente madura e estável, mas que nunca teve adoção de mercado em massa — seu uso sempre foi concentrado em nichos de IA simbólica.

## Ecossistema e ferramentas
- **[SWI-Prolog](https://www.swi-prolog.org/)**: implementação de referência, gratuita, com IDE, depurador, profiler e ambiente web interativo ([SWISH](https://swish.swi-prolog.org/)). É a que usamos neste trabalho.
- **[GNU Prolog](http://www.gprolog.org/)**, **[SICStus](https://sicstus.sics.se/)**, **[ECLiPSe](https://eclipseclp.org/)**: alternativas focadas em executáveis leves ou em programação por restrições.
- **Interoperabilidade com Python**: a biblioteca **[janus_swi](https://www.swi-prolog.org/pldoc/man?section=janus-python-package)** permite chamadas bidirecionais rápidas entre Prolog e Python (é a que usamos para consultar a base de conhecimento). A alternativa mais antiga, **[PySwip](https://github.com/yuce/pyswip)**, é mais lenta e menos segura, pois se comunica via strings.

## Comunidade
Pequena, mas ativa: [fórum oficial da SWI-Prolog](https://swi-prolog.discourse.group/), [tag no Stack Overflow](https://stackoverflow.com/questions/tagged/prolog). Volume de conteúdo e bibliotecas de terceiros é muito menor do que em linguagens mainstream como Python.

## Perspectivas de adoção
No [TIOBE Index](https://www.tiobe.com/tiobe-index/), Prolog fica tipicamente fora do top 20 (posição ~20-35, <1% de participação) — hoje é uma linguagem de nicho no mercado geral. Por outro lado, há interesse renovado com a IA **neuro-simbólica**, que busca unir aprendizado de máquina com raciocínio lógico explicável — algo que modelos estatísticos puros não entregam.

## Limitações
- Curva de aprendizado alta (mudança de raciocínio imperativo → lógico)
- Performance inferior a linguagens compiladas em tarefas pesadas
- Poucas vagas de emprego pedindo Prolog como linguagem principal
- Depuração pouco intuitiva por causa do backtracking automático

## Conclusão
Prolog é maduro tecnicamente, tem ecossistema pequeno mas funcional e comunidade reduzida. Sua adoção geral é marginal, mas seu nicho — raciocínio explicável baseado em regras — continua tendo valor exatamente em casos como o nosso: um diagnóstico médico onde entender *por que* o sistema chegou àquela conclusão é tão importante quanto a conclusão em si.

## Fontes
- [SWI-Prolog — Status and releases](https://www.swi-prolog.org/pldoc/man?section=status)
- [SWI-Prolog — Interfacing to Python](https://www.swi-prolog.org/FAQ/Python.md)
- [TIOBE Index](https://www.tiobe.com/tiobe-index/)
- [SWI-Prolog Community](https://www.swi-prolog.org/community.html)

