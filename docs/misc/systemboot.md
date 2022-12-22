---
layout: default
title: System Bootprobleme
parent: Misc
---

# {{ page.title }}

______________________________________________________________________

{: .note }

> Wenn der Windows Bootloader defekt ist, kann er mit einen Installationsstick
> Wiederhergestellt werden

______________________________________________________________________

Windows Installationsmedium starten und folgende Befehle ausführen um den gesammten Windows Bootloader neu zu installieren

```
diskpart
list volume
select volume (EFI-PARTITION)
assign letter S
exit
bcdboot C:\windows /s S:
remove letter S
```
