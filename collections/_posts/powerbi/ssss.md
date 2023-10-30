A partir do número de níveis existentes, é possível criar uma sequência de funções DAX para resolver o problemas

https://community.fabric.microsoft.com/t5/Desktop/Create-new-table-based-on-Distinct-of-two-columns-from-other/m-p/211599

Assuntos CNMP Nível 1-2 =
FILTER(
SUMMARIZE('Assuntos CNMP','Assuntos CNMP'[Calc_Level1],'Assuntos CNMP'[Calc_Level2]),
NOT(ISBLANK('Assuntos CNMP'[Calc_Level2]))
)
