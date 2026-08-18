% =========================================================
% Regras de Inferência - Sistema de Diagnóstico por Sintomas
% =========================================================

% ---------------------------------------------------------
% CARREGAMENTO DA BASE DE CONHECIMENTO
% ---------------------------------------------------------
:- prolog_load_context(directory, Diretorio),
   directory_file_path(Diretorio, '../base_conhecimento/doencas.pl', ArquivoDoencas),
   consult(ArquivoDoencas).


% =========================================================
% BUSCA DE SINTOMAS PARA O PYTHON
% =========================================================

% Predicado auxiliar mantido para compatibilidade com o Python
sintoma(Doenca, Sintoma) :-
    sintoma(Doenca, Sintoma, _, _).


% =========================================================
% VALIDAÇÃO E CÁLCULO DE PONTUAÇÃO PONDERADA
% =========================================================

% calcula_pontuacao(+Doenca, +SintomasInformados, -Pontuacao)
%
% Retorna a compatibilidade em % ponderada pelos pesos.
% Falha (descarta) se faltar algum sintoma OBRIGATÓRIO.

calcula_pontuacao(Doenca, SintomasInformados, Pontuacao) :-
    % 1. Checa se o usuário atendeu TODOS os sintomas obrigatórios da doença
    \+ (sintoma(Doenca, S_Obrigatorio, _, sim), \+ member(S_Obrigatorio, SintomasInformados)),

    % 2. Soma os pesos totais da doença
    findall(Peso, sintoma(Doenca, _, Peso, _), ListaPesosTotais),
    sum_list(ListaPesosTotais, PesoMaximo),
    PesoMaximo > 0,

    % 3. Soma os pesos dos sintomas que o usuário realmente apresentou
    findall(
        Peso,
        (
            sintoma(Doenca, Sintoma, Peso, _),
            member(Sintoma, SintomasInformados)
        ),
        ListaPesosUsuario
    ),
    sum_list(ListaPesosUsuario, PesoObtido),

    % Precisa ter pelo menos um sintoma presente
    PesoObtido > 0,

    % 4. Calcula a porcentagem ponderada arredondada
    PorcentagemCalculada is (PesoObtido / PesoMaximo) * 100,
    Pontuacao is round(PorcentagemCalculada * 10) / 10.


% =========================================================
% GERAÇÃO DO RANKING
% =========================================================

% diagnosticar(+SintomasInformados, -ResultadosOrdenados)
%
% Retorna as doenças compatíveis ordenadas do maior para o menor %

diagnosticar(SintomasInformados, ResultadosOrdenados) :-
    findall(
        Pontuacao-Doenca,
        (
            doenca(Doenca),
            calcula_pontuacao(Doenca, SintomasInformados, Pontuacao)
        ),
        Resultados
    ),
    ordenar_resultados(Resultados, ResultadosOrdenados).


% =========================================================
% ORDENAÇÃO
% =========================================================

ordenar_resultados(Resultados, ResultadosOrdenados) :-
    keysort(Resultados, Crescente),
    reverse(Crescente, ResultadosOrdenados).


% =========================================================
% TOP N
% =========================================================

diagnosticar_top(SintomasInformados, N, TopN) :-
    diagnosticar(SintomasInformados, Todos),
    (
        length(Prefixo, N),
        append(Prefixo, _, Todos)
    ->
        TopN = Prefixo
    ;
        TopN = Todos
    ).