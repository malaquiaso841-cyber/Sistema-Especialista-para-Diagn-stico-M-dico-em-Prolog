# Sistemas Especialistas

## Conceito

Um sistema especialista é um programa desenvolvido para representar o conhecimento e o raciocínio de um especialista em determinada área.

Ele utiliza uma base de conhecimento e regras de inferência para analisar informações e apresentar possíveis conclusões.

## Componentes principais

Um sistema especialista normalmente possui:

- **Base de conhecimento:** armazena fatos e informações sobre o domínio;
- **Motor de inferência:** aplica regras sobre os fatos cadastrados;
- **Interface:** permite a interação entre o usuário e o sistema;
- **Explicação dos resultados:** apresenta as conclusões geradas.

## Aplicação no projeto

Neste projeto, a base de conhecimento está no arquivo:

```text
prolog/base_conhecimento/doencas.pl
```

Ela armazena as doenças, os sintomas, seus pesos e a indicação de sintomas obrigatórios.

O motor de inferência está em:

```text
prolog/regras/inferencia.pl
```

Ele compara os sintomas selecionados, calcula a compatibilidade e gera um ranking de possíveis doenças.

O Python disponibiliza duas formas de interação:

- `main.py`: interface pelo terminal;
- `python/interface.py`: interface gráfica.

## Funcionamento resumido

```mermaid
flowchart LR
    A["Usuário informa sintomas"] --> B["Base de conhecimento"]
    B --> C["Motor de inferência"]
    C --> D["Ranking de compatibilidade"]
```

## Limitações

O sistema depende das informações previamente cadastradas e não possui o conhecimento completo de um profissional.

Neste projeto, os resultados são apenas educacionais e não substituem avaliação ou diagnóstico médico.