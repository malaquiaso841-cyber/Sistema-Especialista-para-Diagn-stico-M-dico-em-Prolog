# Integração entre Python e Prolog

O sistema utiliza a biblioteca *PySwip* para permitir a comunicação entre Python e SWI-Prolog.

O Python recebe os sintomas pela interface e cria uma consulta Prolog:

python
lista_prolog = "[" + ",".join(sintomas) + "]"
consulta = f"diagnosticar({lista_prolog}, R)"
resultados = list(prolog.query(consulta))


O arquivo inferencia.pl consulta a base doencas.pl, verifica os sintomas obrigatórios, calcula as porcentagens e devolve um ranking.

O fluxo da integração é:

1. O usuário seleciona os sintomas;
2. O Python converte os sintomas para uma lista Prolog;
3. O PySwip envia a consulta;
4. O Prolog executa as regras de inferência;
5. O resultado retorna ao Python;
6. A interface apresenta o ranking.

mermaid
flowchart LR
    A["Interface Python"] --> B["PySwip"]
    B --> C["inferencia.pl"]
    C --> D["doencas.pl"]
    D --> C
    C --> B
    B --> A
