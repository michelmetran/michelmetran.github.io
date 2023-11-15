---
title: "PowerBI: Path Functions"
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-09-07T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
  - Data Science
tags:
  - Power BI
  - DAX
---

Uma vez que eu organizei uma tabela usando as funções de HierarchyId, é possível reproduzir a hierarquia no Power BI, utilizando as funções _Path_.

Inicialmente criamos duas colunas básicas, contendo o _path_ e a profundidade dos assuntos, ou seja, quantos níveis existem?!

```m
Calc__Path = PATH('Assuntos CNMP'[IdAssuntoCNMP], 'Assuntos CNMP'[IdPaiCNMP])
Calc__Lenght = PATHLENGTH ('Assuntos CNMP'[Calc__Path])
```

<br>

A partir do número de níveis existentes, é possível criar uma sequência de funções DAX para resolver o problemas

```m
Calc_Level1 = LOOKUPVALUE(
    'Assuntos CNMP'[AssuntoId],
    'Assuntos CNMP'[IdAssuntoCNMP], PATHITEM ( 'Assuntos CNMP'[Calc__Path], 1, INTEGER )
)

Calc_Level2 =
IF ( PATHLENGTH ('Assuntos CNMP'[Calc__Path]) >= 2,
LOOKUPVALUE(
    'Assuntos CNMP'[AssuntoId],
    'Assuntos CNMP'[IdAssuntoCNMP], PATHITEM ('Assuntos CNMP'[Calc__Path], 2, INTEGER )
),
BLANK()
)

Calc_Level3 =
IF ( PATHLENGTH ('Assuntos CNMP'[Calc__Path]) >= 3,
LOOKUPVALUE(
    'Assuntos CNMP'[AssuntoId],
    'Assuntos CNMP'[IdAssuntoCNMP], PATHITEM ('Assuntos CNMP'[Calc__Path], 3, INTEGER )
),
BLANK()
)

Calc_Level4 =
IF ( PATHLENGTH ('Assuntos CNMP'[Calc__Path]) >= 4,
LOOKUPVALUE(
    'Assuntos CNMP'[AssuntoId],
    'Assuntos CNMP'[IdAssuntoCNMP], PATHITEM ('Assuntos CNMP'[Calc__Path], 4, INTEGER )
),
BLANK()
)

Calc_Level5 =
IF ( PATHLENGTH ('Assuntos CNMP'[Calc__Path]) >= 5,
LOOKUPVALUE(
    'Assuntos CNMP'[AssuntoId],
    'Assuntos CNMP'[IdAssuntoCNMP], PATHITEM ( 'Assuntos CNMP'[Calc__Path], 5, INTEGER )
),
BLANK()
)

Calc_Level6 =
IF ( PATHLENGTH ('Assuntos CNMP'[Calc__Path]) >= 6,
LOOKUPVALUE(
    'Assuntos CNMP'[AssuntoId],
    'Assuntos CNMP'[IdAssuntoCNMP], PATHITEM ( 'Assuntos CNMP'[Calc__Path], 6, INTEGER )
),
BLANK()
)

Calc_Level7 =
IF ( PATHLENGTH ('Assuntos CNMP'[Calc__Path]) >= 7,
LOOKUPVALUE(
    'Assuntos CNMP'[AssuntoId],
    'Assuntos CNMP'[IdAssuntoCNMP], PATHITEM ( 'Assuntos CNMP'[Calc__Path], 7, INTEGER )
),
BLANK()
)

Calc_Level8 =
IF ( PATHLENGTH ('Assuntos CNMP'[Calc__Path]) >= 8,
LOOKUPVALUE(
    'Assuntos CNMP'[AssuntoId],
    'Assuntos CNMP'[IdAssuntoCNMP], PATHITEM ( 'Assuntos CNMP'[Calc__Path], 8, INTEGER )
),
BLANK()
)
```

<br>

[DAX's PATH function equivalent Custom Column in Power Query](https://community.fabric.microsoft.com/t5/Quick-Measures-Gallery/DAX-s-PATH-function-equivalent-Custom-Column-in-Power-Query/m-p/800386)

Uma vez construída essa tabela, é possível criar uma segmentação de dados utilizando um _plugin_ que remove os _blanks_. O plugin se chama [Hierarchy Slicer](https://azurebi-docs.jppp.org/powerbi-visuals/hierarchy-slicer.html).

Tomei conhecimento dele através do vídeo [Handling Empty Members and Ragged Hierarchies in a Hierarchy Slicer](https://www.youtube.com/watch?v=Q-fT10OI6uI), do canal [@HavensConsulting](https://www.youtube.com/@HavensConsulting). Esse canal também apresentou um vídeo sobre o tema, utilizando uma segmentação de dados "nativa" do Power BI. Contudo, não atende plenamente devido aos "brancos".

O repositório do GitHub é o [azurebi-docs](https://github.com/liprec/azurebi-docs/issues).

*TODO*: Preciso descobrir como colocar o campo de pesquisa.
