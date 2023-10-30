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
Calc__Path = PATH(Assunto[IdAssuntoCNMP], Assunto[IdPaiCNMP])
Calc__Lenght = PATHLENGTH (Assunto[Calc__Path] )
```

<br>

A partir do número de níveis existentes, é possível criar uma sequência de funções DAX para resolver o problemas

```m
Calc_Level1 = LOOKUPVALUE(
    Assunto[AssuntoId],
    Assunto[IdAssuntoCNMP], PATHITEM ( Assunto[Calc__Path], 1, INTEGER )
)

Calc_Level2 =
IF ( PATHLENGTH (Assunto[Calc__Path] ) >= 2,
LOOKUPVALUE(
    Assunto[AssuntoId],
    Assunto[IdAssuntoCNMP], PATHITEM ( Assunto[Calc__Path], 2, INTEGER )
),
CONCATENATE("..", Assunto[Calc_Level1])
)

Calc_Level3 =
IF ( PATHLENGTH (Assunto[Calc__Path] ) >= 3,
LOOKUPVALUE(
    Assunto[AssuntoId],
    Assunto[IdAssuntoCNMP], PATHITEM ( Assunto[Calc__Path], 3, INTEGER )
),
CONCATENATE("..", Assunto[Calc_Level2])
)

Calc_Level4 =
IF ( PATHLENGTH (Assunto[Calc__Path] ) >= 4,
LOOKUPVALUE(
    Assunto[AssuntoId],
    Assunto[IdAssuntoCNMP], PATHITEM ( Assunto[Calc__Path], 4, INTEGER )
),
CONCATENATE("..", Assunto[Calc_Level3])
)

Calc_Level5 =
IF ( PATHLENGTH (Assunto[Calc__Path] ) >= 5,
LOOKUPVALUE(
    Assunto[AssuntoId],
    Assunto[IdAssuntoCNMP], PATHITEM ( Assunto[Calc__Path], 5, INTEGER )
),
CONCATENATE("..", Assunto[Calc_Level4])
)

Calc_Level6 =
IF ( PATHLENGTH (Assunto[Calc__Path] ) >= 6,
LOOKUPVALUE(
    Assunto[AssuntoId],
    Assunto[IdAssuntoCNMP], PATHITEM ( Assunto[Calc__Path], 6, INTEGER )
),
CONCATENATE("..", Assunto[Calc_Level5])
)

Calc_Level7 =
IF ( PATHLENGTH (Assunto[Calc__Path] ) >= 7,
LOOKUPVALUE(
    Assunto[AssuntoId],
    Assunto[IdAssuntoCNMP], PATHITEM ( Assunto[Calc__Path], 7, INTEGER )
),
CONCATENATE("..", Assunto[Calc_Level6])
)

Calc_Level8 =
IF ( PATHLENGTH (Assunto[Calc__Path] ) >= 8,
LOOKUPVALUE(
    Assunto[AssuntoId],
    Assunto[IdAssuntoCNMP], PATHITEM ( Assunto[Calc__Path], 8, INTEGER )
),
CONCATENATE("..", Assunto[Calc_Level7])
)
```

[DAX's PATH function equivalent Custom Column in Power Query](https://community.fabric.microsoft.com/t5/Quick-Measures-Gallery/DAX-s-PATH-function-equivalent-Custom-Column-in-Power-Query/m-p/800386)
