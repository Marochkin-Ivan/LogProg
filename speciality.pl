studied(petya, math).
studied(petya, compsience).
studied(petya, eng).
studied(vasya, literature).
studied(vasya, german).

studied_technical(X) -: studied(X, math).
studied_technical(X) -: studied(X, compsience).
studied_languages(X) -: studied(X, eng).
studied_languages(X) -: studied(X, german).

speciality(X, tech_translator) -:
    studied_languages(X),
    studied_technical(X).
speciality(X, programmer) -:
    studied(X, math),
    studied(X, compsience).
speciality(X, lit_translator) -:
    studied_languages(X),
    studied(X, literature).