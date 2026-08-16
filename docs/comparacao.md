# Comparação com Outras Tecnologias

## 1. Introdução

Uma das propostas deste projeto é compreender as características da linguagem Prolog e identificar suas diferenças em relação a outras tecnologias utilizadas no desenvolvimento de software.

Para isso, Prolog é comparado principalmente com Python e com o paradigma de programação imperativa.

---

## 2. Prolog vs Python

Prolog e Python possuem características bastante diferentes.

Prolog é baseado principalmente em programação lógica, enquanto Python é uma linguagem multiparadigma de propósito geral.

Em Prolog, fatos e regras podem ser utilizados para representar conhecimento diretamente.

Em Python, essa representação precisa ser construída por meio de estruturas da própria linguagem, como funções, classes, listas, dicionários e outras estruturas de dados.

| Característica         | Prolog            | Python                          |
| ---------------------- | ----------------- | ------------------------------- |
| Paradigma principal    | Lógico            | Multiparadigma                  |
| Foco                   | Relações e regras | Propósito geral                 |
| Fatos                  | Nativos           | Precisam ser implementados      |
| Regras                 | Nativas           | Precisam ser implementadas      |
| Inferência lógica      | Integrada         | Não é o foco da linguagem       |
| Backtracking           | Integrado         | Não é mecanismo central         |
| Sistemas especialistas | Boa adequação     | Pode ser utilizado              |
| Interfaces             | Mais limitada     | Grande variedade de bibliotecas |
| Uso geral              | Mais específico   | Muito amplo                     |

---

## 3. Prolog vs Java

Java é uma linguagem de programação de propósito geral baseada principalmente em orientação a objetos.

Enquanto Java normalmente exige que o programador descreva de forma mais explícita as operações realizadas pelo programa, Prolog permite representar relações por meio de fatos e regras e utilizar seu mecanismo de inferência para procurar soluções.

Java possui ampla utilização em:

* sistemas empresariais;
* aplicações web;
* aplicações Android;
* sistemas distribuídos;
* aplicações de grande porte.

Prolog é mais específico para situações em que representação de conhecimento, relações e regras possuem papel central.

---

## 4. Programação lógica vs programação imperativa

Na programação imperativa, o programa normalmente descreve uma sequência de instruções que devem ser executadas.

Em programação lógica, o programador descreve principalmente informações e relações que representam o problema.

### Programação imperativa

Um programa imperativo pode seguir uma sequência semelhante a:

```text
Receber dados
↓
Processar dados
↓
Executar condição
↓
Calcular resultado
↓
Exibir resultado
```

### Programação lógica

Em uma abordagem lógica, o programa pode representar:

```text
Fatos
+
Regras
+
Consulta
↓
Inferência
↓
Resultado
```

Essa diferença representa uma mudança importante na forma de pensar e desenvolver programas.

---

## 5. Vantagens do Prolog

Entre as vantagens identificadas durante a pesquisa estão:

* representação direta de fatos;
* representação direta de regras;
* mecanismo de inferência integrado;
* unificação;
* backtracking;
* boa adequação a sistemas baseados em conhecimento;
* código compacto em determinados problemas;
* facilidade para representar relações.

---

## 6. Desvantagens do Prolog

Entre as limitações estão:

* menor popularidade no desenvolvimento comercial em comparação com linguagens como Python, Java e JavaScript;
* paradigma diferente da programação tradicional;
* curva de adaptação para programadores iniciantes;
* não é adequado para todos os tipos de aplicações;
* algumas tarefas podem ser mais simples de implementar em linguagens de propósito geral.

---

## 7. Quando utilizar Prolog?

Prolog pode ser uma boa opção quando o problema possui características como:

* grande quantidade de regras;
* relações entre informações;
* representação de conhecimento;
* necessidade de busca de soluções;
* sistemas especialistas;
* problemas de lógica;
* inteligência artificial simbólica.

O sistema desenvolvido neste projeto é um exemplo desse tipo de aplicação.

---

## 8. Quando não utilizar Prolog?

Prolog pode não ser a melhor opção quando o objetivo principal é:

* desenvolvimento de interfaces modernas;
* aplicações web convencionais;
* desenvolvimento de aplicativos móveis;
* processamento numérico intensivo;
* desenvolvimento de sistemas empresariais tradicionais;
* projetos que dependem de um ecossistema específico de bibliotecas.

Nesses casos, linguagens de propósito geral podem oferecer ferramentas mais adequadas.

---

## 9. Prolog no projeto

A escolha do Prolog está relacionada diretamente ao objetivo da aplicação.

O sistema precisa representar relações entre:

```text
Doenças
   ↕
Sintomas
```

Além disso, precisa utilizar regras para encontrar possíveis correspondências.

Essas características são compatíveis com a programação lógica, permitindo que o projeto demonstre de maneira prática as principais características da linguagem.

---

## 10. Conclusão

A comparação demonstra que Prolog possui uma abordagem diferente de linguagens como Python e Java.

Enquanto linguagens de propósito geral são adequadas para uma grande variedade de aplicações, Prolog apresenta características especialmente interessantes para problemas baseados em lógica, relações, regras e representação de conhecimento.

Por esse motivo, Prolog foi considerado adequado para o desenvolvimento do sistema especialista apresentado neste projeto.
