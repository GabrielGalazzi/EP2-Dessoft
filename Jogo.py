def normaliza(dic):
    dicpais = {}
    for continente in dic:
        for pais in dic[continente]:
            dicpais[pais] = dic[continente][pais]
            dicpais[pais]['Continente'] = str(continente)
    return dicpais
