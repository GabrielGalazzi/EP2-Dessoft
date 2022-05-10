import random
import math
ex = {
  "asia": {
    "afeganistao": {
      "area": 652230,
      "populacao": 31390200,
      "capital": "Cabul",
      "geo": {
        "latitude": 33.93911,
        "longitude": 67.709953
      },
      "bandeira": {
        "vermelha": 28,
        "laranja": 1,
        "amarela": 0,
        "verde": 33,
        "azul": 0,
        "azul claro": 0,
        "preta": 33,
        "branca": 3,
        "outras": 5
      }
    },
    "arabia saudita": {
      "area": 2149690,
      "populacao": 34268528,
      "capital": "Riade",
      "geo": {
        "latitude": 23.885942,
        "longitude": 45.079162
      },
      "bandeira": {
        "vermelha": 0,
        "laranja": 0,
        "amarela": 0,
        "verde": 94,
        "azul": 0,
        "azul claro": 0,
        "preta": 0,
        "branca": 5,
        "outras": 2
      }
    }
  },
  "oceania": {
    "australia": {
      "area": 7692024,
      "populacao": 25364307,
      "capital": "Camberra",
      "geo": {
        "latitude": -25.274398,
        "longitude": 133.775136
      },
      "bandeira": {
        "vermelha": 9,
        "laranja": 0,
        "amarela": 0,
        "verde": 0,
        "azul": 79,
        "azul claro": 0,
        "preta": 0,
        "branca": 11,
        "outras": 3
      }
    }
  }
}
def normaliza(dic):
    dicpais = {}
    for continente in dic:
        for pais in dic[continente]:
            dicpais[pais] = dic[continente][pais]
            dicpais[pais]['Continente'] = str(continente)
    return dicpais
def sorteia_pais(dic):
    dicpais = normaliza(dic)
    l_pais = list(dicpais.keys())
    pais = random.choice(l_pais)
    return pais
def haversine(r,p1,l1,p2,l2):
    p1 = math.radians(p1)
    p2 = math.radians(p2)
    l1 = math.radians(l1)
    l2 = math.radians(l2)
    dist = 2 * r * math.asin(((math.sin((p2-p1)/2)**2) + math.cos(p1) * math.cos(p2) * (math.sin((l2-l1)/2) ** 2))** 0.5)
    
    return dist
def adiciona_em_ordem(pais,dist,l):
    l2 = [[pais,dist]]
    if l2[0][0] in l:
        return l2[0]
    elif l == []:
        l.append(l2[0])
        return l
    else:
      for i in range(len(l)):
            print(i)
            if l[i][1]<l2[0][1]:
             0
            else:
                l.insert(i,l2[0])
                return l            