
% SISTEMA ESPECIALISTA - DIAGNOSTICO

% DOENCAS

doenca(gripe).
doenca(resfriado).
doenca(dengue).
doenca(covid_19).
doenca(pneumonia).
doenca(sinusite).
doenca(amigdalite).
doenca(bronquite).
doenca(asma).
doenca(enxaqueca).


% SINTOMAS


% Gripe
sintoma(gripe, febre).
sintoma(gripe, tosse).
sintoma(gripe, dor_garganta).
sintoma(gripe, dor_muscular).
sintoma(gripe, fadiga).

% Resfriado
sintoma(resfriado, coriza).
sintoma(resfriado, espirros).
sintoma(resfriado, congestao_nasal).
sintoma(resfriado, dor_garganta).
sintoma(resfriado, tosse).

% Dengue
sintoma(dengue, febre_alta).
sintoma(dengue, dor_cabeca).
sintoma(dengue, dor_atras_olhos).
sintoma(dengue, dor_muscular).
sintoma(dengue, manchas_pele).

% COVID-19
sintoma(covid_19, febre).
sintoma(covid_19, tosse).
sintoma(covid_19, fadiga).
sintoma(covid_19, dor_garganta).
sintoma(covid_19, perda_olfato).

% Pneumonia
sintoma(pneumonia, febre).
sintoma(pneumonia, tosse).
sintoma(pneumonia, falta_ar).
sintoma(pneumonia, dor_peito).
sintoma(pneumonia, calafrios).

% Sinusite
sintoma(sinusite, congestao_nasal).
sintoma(sinusite, dor_facial).
sintoma(sinusite, dor_cabeca).
sintoma(sinusite, secrecao_nasal).
sintoma(sinusite, reducao_olfato).

% Amigdalite
sintoma(amigdalite, dor_garganta).
sintoma(amigdalite, dificuldade_engolir).
sintoma(amigdalite, febre).
sintoma(amigdalite, amigdalas_inchadas).
sintoma(amigdalite, mau_halito).

% Bronquite
sintoma(bronquite, tosse).
sintoma(bronquite, catarro).
sintoma(bronquite, falta_ar).
sintoma(bronquite, chiado_peito).
sintoma(bronquite, fadiga).

% Asma
sintoma(asma, falta_ar).
sintoma(asma, chiado_peito).
sintoma(asma, tosse).
sintoma(asma, aperto_peito).
sintoma(asma, dificuldade_respirar).

% Enxaqueca
sintoma(enxaqueca, dor_cabeca_intensa).
sintoma(enxaqueca, nausea).
sintoma(enxaqueca, sensibilidade_luz).
sintoma(enxaqueca, sensibilidade_som).
sintoma(enxaqueca, alteracoes_visuais).

doenca(gastrite, [
    dor_abdominal,
    azia,
    nausea,
    sensacao_estomago_cheio,
    perda_de_apetite
]). 

doenca(refluxo_gastroesofagico, [
    azia,
    regurgitacao,
    dor_no_peito,
    tosse,
    dificuldade_para_engolir
]).

doenca(gastroenterite, [
    diarreia,
    vomitos,
    dor_abdominal,
    nausea,
    febre
]). 

doenca(intoxicacao_alimentar, [
    nausea,
    vomitos,
    diarreia,
    dor_abdominal,
    febre
]).

doenca(infeccao_urinaria, [
    ardencia_ao_urinar,
    vontade_frequente_de_urinar,
    dor_abdominal,
    urina_turva,
    dor_ao_urinar
]).

doenca(cistite, [
    ardencia_ao_urinar,
    urgencia_urinaria,
    dor_pelvica,
    urina_turva,
    aumento_frequencia_urinaria
]). 

doenca(amigdalite_bacteriana, [
    dor_de_garganta,
    febre,
    dificuldade_para_engolir,
    placas_nas_amigdalas,
    ganglios_inchados
]). 

doenca(otite, [
    dor_de_ouvido,
    febre,
    perda_de_audicao,
    sensacao_ouvido_tampado,
    secrecao_no_ouvido
]).

doenca(conjuntivite, [
    olhos_vermelhos,
    coceira_nos_olhos,
    lacrimejamento,
    secrecao_ocular,
    sensacao_areia_nos_olhos
]).

doenca(rinite_alergica, [
    espirros,
    coriza,
    coceira_no_nariz,
    congestao_nasal,
    coceira_nos_olhos
]). 

doenca(dermatite, [
    coceira_na_pele,
    vermelhidao,
    ressecamento,
    descamacao,
    irritacao
]).

doenca(urticaria, [
    manchas_vermelhas,
    coceira,
    inchaco,
    placas_na_pele,
    sensacao_de_ardencia
]).

doenca(catapora, [
    febre,
    manchas_vermelhas,
    bolhas_na_pele,
    coceira,
    mal_estar
]).

doenca(sarampo, [
    febre,
    tosse,
    coriza,
    olhos_vermelhos,
    manchas_na_pele
]).

doenca(rubeola, [
    febre_baixa,
    manchas_na_pele,
    dor_de_cabeca,
    ganglios_inchados,
    dor_nas_articulacoes
]).

doenca(caxumba, [
    inchaco_no_rosto,
    dor_na_mandibula,
    febre,
    dor_de_cabeca,
    dificuldade_para_mastigar
]).

doenca(faringite, [
    dor_de_garganta,
    dificuldade_para_engolir,
    febre,
    rouquidao,
    ganglios_inchados
]).

doenca(laringite, [
    rouquidao,
    perda_da_voz,
    tosse_seca,
    dor_de_garganta,
    dificuldade_para_falar
]).

doenca(tuberculose, [
    tosse_persistente,
    febre,
    suor_noturno,
    perda_de_peso,
    cansaco
]).

doenca(anemia, [
    fadiga,
    fraqueza,
    palidez,
    tontura,
    falta_de_ar
]).
