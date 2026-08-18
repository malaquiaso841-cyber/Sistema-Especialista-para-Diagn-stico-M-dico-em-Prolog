% =========================================================
% Base de Conhecimento - Sistema de Diagnóstico por Sintomas
% =========================================================

% ---------------------------------------------------------
% Fatos: doenca/1
% ---------------------------------------------------------
doenca(gripe).
doenca(resfriado).
doenca(covid19).
doenca(sinusite).
doenca(faringite).
doenca(bronquite).
doenca(pneumonia).
doenca(asma).
doenca(rinite_alergica).
doenca(conjuntivite).
doenca(gastroenterite).
doenca(intoxicacao_alimentar).
doenca(refluxo).
doenca(gastrite).
doenca(enxaqueca).
doenca(hipertensao).
doenca(diabetes).
doenca(infeccao_urinaria).
doenca(anemia).
doenca(dengue).

% ---------------------------------------------------------
% Fatos: sintoma(Doenca, Sintoma, Peso, Obrigatorio)
%
% Peso: 1 (Genérico) a 5 (Muito Específico/Patognomônico)
% Obrigatorio: sim (Condição eliminatória) / nao
% ---------------------------------------------------------

% gripe
sintoma(gripe, febre, 3, nao).
sintoma(gripe, calafrio, 2, nao).
sintoma(gripe, dor_cabeca, 2, nao).
sintoma(gripe, dor_muscular, 3, nao).
sintoma(gripe, tosse, 2, nao).

% resfriado
sintoma(resfriado, espirro, 4, nao).
sintoma(resfriado, coriza, 4, nao).
sintoma(resfriado, dor_garganta, 3, nao).
sintoma(resfriado, tosse, 2, nao).
sintoma(resfriado, congestao_nasal, 3, nao).

% covid19
sintoma(covid19, febre, 2, nao).
sintoma(covid19, tosse, 2, nao).
sintoma(covid19, perda_olfato, 5, nao).      % Altamente específico
sintoma(covid19, perda_paladar, 5, nao).     % Altamente específico
sintoma(covid19, fadiga, 2, nao).

% sinusite
sintoma(sinusite, dor_cabeca, 3, nao).
sintoma(sinusite, congestao_nasal, 4, nao).
sintoma(sinusite, dor_facial, 5, sim).       % Sintoma chave
sintoma(sinusite, coriza, 3, nao).
sintoma(sinusite, febre, 2, nao).

% faringite
sintoma(faringite, dor_garganta, 5, sim).    % Sintoma chave
sintoma(faringite, febre, 2, nao).
sintoma(faringite, dificuldade_engolir, 4, nao).
sintoma(faringite, ganglios_inchados, 4, nao).
sintoma(faringite, tosse, 2, nao).

% bronquite
sintoma(bronquite, tosse, 4, sim).           % Sintoma chave
sintoma(bronquite, chiado_peito, 4, nao).
sintoma(bronquite, falta_ar, 3, nao).
sintoma(bronquite, dor_peito, 2, nao).
sintoma(bronquite, fadiga, 2, nao).

% pneumonia
sintoma(pneumonia, febre, 3, nao).
sintoma(pneumonia, tosse, 3, nao).
sintoma(pneumonia, falta_ar, 4, nao).
sintoma(pneumonia, dor_peito, 4, nao).
sintoma(pneumonia, calafrio, 3, nao).

% asma
sintoma(asma, falta_ar, 4, nao).
sintoma(asma, chiado_peito, 5, sim).        % Sintoma chave
sintoma(asma, tosse, 2, nao).
sintoma(asma, aperto_peito, 3, nao).
sintoma(asma, dificuldade_respirar, 4, nao).

% rinite_alergica
sintoma(rinite_alergica, espirro, 4, nao).
sintoma(rinite_alergica, coriza, 4, nao).
sintoma(rinite_alergica, coceira_olhos, 4, nao).
sintoma(rinite_alergica, congestao_nasal, 3, nao).
sintoma(rinite_alergica, coceira_nariz, 5, nao).

% conjuntivite
sintoma(conjuntivite, olho_vermelho, 5, sim).  % Sintoma chave
sintoma(conjuntivite, coceira_olhos, 4, nao).
sintoma(conjuntivite, lacrimejamento, 3, nao).
sintoma(conjuntivite, secrecao_ocular, 4, nao).
sintoma(conjuntivite, sensibilidade_luz, 3, nao).

% gastroenterite
sintoma(gastroenterite, diarreia, 5, nao).
sintoma(gastroenterite, nausea, 3, nao).
sintoma(gastroenterite, vomito, 4, nao).
sintoma(gastroenterite, dor_abdominal, 3, nao).
sintoma(gastroenterite, febre, 2, nao).

% intoxicacao_alimentar
sintoma(intoxicacao_alimentar, nausea, 3, nao).
sintoma(intoxicacao_alimentar, vomito, 5, nao).
sintoma(intoxicacao_alimentar, diarreia, 4, nao).
sintoma(intoxicacao_alimentar, dor_abdominal, 3, nao).
sintoma(intoxicacao_alimentar, calafrio, 2, nao).

% refluxo
sintoma(refluxo, azia, 5, sim).             % Sintoma chave
sintoma(refluxo, dor_peito, 3, nao).
sintoma(refluxo, regurgitacao, 5, nao).
sintoma(refluxo, dificuldade_engolir, 3, nao).
sintoma(refluxo, tosse, 1, nao).

% gastrite
sintoma(gastrite, dor_abdominal, 4, nao).
sintoma(gastrite, nausea, 3, nao).
sintoma(gastrite, azia, 5, sim).            % Sintoma chave
sintoma(gastrite, perda_apetite, 2, nao).
sintoma(gastrite, inchaco_abdominal, 3, nao).

% enxaqueca
sintoma(enxaqueca, dor_cabeca, 5, sim).      % Sintoma chave
sintoma(enxaqueca, sensibilidade_luz, 4, nao).
sintoma(enxaqueca, nausea, 3, nao).
sintoma(enxaqueca, tontura, 2, nao).
sintoma(enxaqueca, sensibilidade_som, 4, nao).

% hipertensao
sintoma(hipertensao, dor_cabeca, 2, nao).
sintoma(hipertensao, tontura, 3, nao).
sintoma(hipertensao, visao_turva, 4, nao).
sintoma(hipertensao, dor_peito, 3, nao).
sintoma(hipertensao, falta_ar, 2, nao).

% diabetes
sintoma(diabetes, sede_excessiva, 5, nao).
sintoma(diabetes, fome_excessiva, 4, nao).
sintoma(diabetes, fadiga, 2, nao).
sintoma(diabetes, visao_turva, 3, nao).
sintoma(diabetes, urinar_frequente, 5, nao).

% infeccao_urinaria
sintoma(infeccao_urinaria, urinar_frequente, 4, nao).
sintoma(infeccao_urinaria, dor_urinar, 5, sim). % Sintoma chave
sintoma(infeccao_urinaria, dor_abdominal, 2, nao).
sintoma(infeccao_urinaria, febre, 2, nao).
sintoma(infeccao_urinaria, urina_turva, 4, nao).

% anemia
sintoma(anemia, fadiga, 4, nao).
sintoma(anemia, palidez, 5, nao).
sintoma(anemia, tontura, 3, nao).
sintoma(anemia, falta_ar, 2, nao).
sintoma(anemia, dor_cabeca, 1, nao).

% dengue
sintoma(dengue, febre, 4, sim).              % Sintoma chave
sintoma(dengue, dor_muscular, 3, nao).
sintoma(dengue, dor_atras_olhos, 5, nao).
sintoma(dengue, dor_cabeca, 2, nao).
sintoma(dengue, manchas_pele, 4, nao).
