---
title: Cheat Sheet
---

PowerShell pipes **objects**, not text. `Get-Process | Where-Object CPU -gt 10` filters on a property; there is no
column parsing as with `grep` and `awk`:

```powershell
Get-Process | Where-Object CPU -gt 10 | Sort-Object CPU -Descending | Select-Object -First 5 Name, CPU
```

## Basics

```powershell
$folder = 'C:\Program Files\Microsoft Office\Office16\'   # single quotes: literal
Write-Host "Folder: $folder"                              # double quotes expand variables

$letters = "a", "b", "c"
foreach ($letter in $letters) {
    Write-Host $letter
}

if ($a -gt 2) {
    Write-Host "$a is greater than 2"
} elseif ($a -eq 2) {
    Write-Host "$a is 2"
} else {
    Write-Host "$a is less than 2 or not set"
}

function Get-Greeting([string]$Name = "World") {
    "Hello $Name"   # values that aren't captured are returned
}
Get-Greeting -Name Ada
```

## Comparison operators

`>` and `<` are redirections in PowerShell, so comparisons use named operators. They are case-insensitive; prefix them
with `c` (`-ceq`) for case-sensitive comparison.

| Operator              | Meaning                      | Example                                |
| --------------------- | ---------------------------- | -------------------------------------- |
| `-eq`, `-ne`          | equal, not equal             | `$name -eq "admin"`                    |
| `-gt`, `-ge`          | greater (or equal)           | `$size -gt 1GB`                        |
| `-lt`, `-le`          | less (or equal)              | `$count -lt 10`                        |
| `-like`               | wildcard match               | `$file -like "*.log"`                  |
| `-match`              | regex match, sets `$Matches` | `$line -match "error (\d+)"`           |
| `-contains`, `-in`    | collection membership        | `$list -contains "x"`, `"x" -in $list` |
| `-and`, `-or`, `-not` | logic                        | `($a -gt 1) -and -not $b`              |

## Useful commands

| Command                                                                                                               | Effect                                     |
| --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| `Get-Help <cmdlet> -Examples`                                                                                         | Usage examples of a cmdlet.                |
| `Get-Command *service*`                                                                                               | Finds cmdlets by name.                     |
| `Get-Process \| Get-Member`                                                                                           | The properties and methods of the objects. |
| `"Test" \| Out-File ./Test.txt`                                                                                       | Writes to a file (`-Append` to append).    |
| `Select-String -Path .\*.txt -Pattern 'Get-'`                                                                         | Searches files, like `grep`.               |
| `Get-ChildItem -Recurse -Filter *.log`                                                                                | Finds files recursively.                   |
| `Get-AppxPackage -Name $app -AllUsers \| Remove-AppxPackage -AllUsers`                                                | Removes a Store app for all users.         |
| `New-Item -Path "HKLM:\Software\Policies\Microsoft\Windows"`                                                          | Creates a registry key.                    |
| `New-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\Windows" -Name 'NoGenTicket' -Value 1 -PropertyType DWord` | Creates a registry value.                  |

:::tip
`Write-Host` writes straight to the console and can't be piped or redirected. To produce output that other commands can
use, just return the value or use `Write-Output`.
:::

:::note
Scripts don't run by default. `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` allows local scripts and signed
downloaded ones.
:::
