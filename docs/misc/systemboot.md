---
layout: default
title: System Boot Problems
parent: Misc
---

# {{ page.title }}

______________________________________________________________________

{: .note }

> If the Windows bootloader is defective, it can be repaired using an installation stick

______________________________________________________________________

Start the Windows installation medium and run the following commands to reinstall the entire Windows bootloader

```
diskpart
list volume
select volume (EFI-PARTITION)
assign letter S
exit
bcdboot C:\windows /s S:
remove letter S
```
