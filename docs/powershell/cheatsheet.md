---
layout: default
title: Cheat Sheet
parent: PowerShell
---

# {{ page.title }}

______________________________________________________________________

Foreach

```powershell
$letterArray = "a","b","c","d"
foreach ($letter in $letterArray)
{
  Write-Host $letter
}
```

If / Else: (-gt (greater than) -eq(equal))

```powershell
if ($a -gt 2) {
  Write-Host "The value $a is greater than 2."
}
else {
  Write-Host ("The value $a is less than or equal to 2," +
    " is not created or is not initialized.")
}
```

Functions

```powershell
function Get-Version($ab, $xy, $1) {
  $PSVersionTable.PSVersion
  Write-Host "${ab} ${xy} ${1}"
}
Get-Version $var1 $var2 $var3
```

Write-Host

`Write-Host "Nachricht"`

Out-File (write to file)

`Write-Host "Test" | Out-File ./Test.txt`

Variables

`$folder = 'C:\Program Files\Microsoft Office\Office16\'`

Remove Apps

`Get-AppxPackage -Name $app -AllUsers | Remove-AppxPackage -AllUsers`

Regestry create new Entry

`New-Item -Path "HKLM:\Software\Policies\Microsoft\"`

Modify Regestry properties

`New-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\" -Name 'NoGenTicket' -Value 1 -PropertyType DWord`

Filter text

`Select-String -Path .\*.txt -Pattern 'Get-'`
