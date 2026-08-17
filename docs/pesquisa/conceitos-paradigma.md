# Funcionamento do Paradigma

Para entender o Prolog e outras linguagens lógicas, é essencial dominar alguns conceitos básicos.

## 1. Conceitos básicos

### 1.1 Fatos

Os **fatos** são declarações que afirmam algo sobre o mundo.

Por exemplo:

```prolog
gato(tom).
```

Nesse caso, o fato afirma que **Tom é um gato**.

### 1.2 Regras

As **regras** definem relações entre fatos.

Por exemplo:

```prolog
animal(X) :- gato(X).
```

Essa regra pode ser interpretada como:

> Se `X` é um gato, então `X` é um animal.

### 1.3 Consultas

As **consultas** são perguntas feitas ao sistema Prolog para verificar se determinada informação é verdadeira ou para encontrar valores que satisfaçam uma determinada condição.

Por exemplo:

```prolog
?- animal(tom).
```

A consulta busca determinar se **Tom é um animal**.

---

## 2. Sintaxe do Prolog

A sintaxe do Prolog é simples e elegante. Um programa Prolog consiste em uma série de **cláusulas**, que podem ser fatos ou regras.

Em Prolog, existe apenas um tipo básico chamado **termo**, que engloba todas as construções sintáticas da linguagem.

Um termo pode ser:

* Uma constante;
* Uma variável;
* Uma estrutura.

### 2.1 Constantes

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

### 2.2 Variáveis

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

### 2.3 Estruturas

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