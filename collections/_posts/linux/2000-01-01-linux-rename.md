---
title: "Linux: *Rename Files*"
---

Códigos necessários para renomear arquivos

```bash
rename 's/Nota de Corretagem //' *.pdf
rename 's/-/./' *.pdf
rename 's/-/./' *.pdf
rename 's/\.pdf$//' *.pdf
rename 's/(.*)/$1 - Nota.pdf/' *
```

Se for renomear fotos usando o Exit

```bash
exiftool -fileOrder DateTimeOriginal -recurse -extension jpg -extension  jpeg -ignoreMinorErrors '-FileName<CreateDate' -d "%Y.%m.%d -  %H.%M.%S %%c".%%le ~/Documents/Andre/
```
