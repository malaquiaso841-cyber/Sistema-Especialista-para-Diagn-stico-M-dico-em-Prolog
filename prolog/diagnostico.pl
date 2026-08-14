
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