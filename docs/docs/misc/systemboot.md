---
layout: default
title: Windows Boot Problems
parent: Misc
---

______________________________________________________________________

## Introduction

If the Windows bootloader is defective, it can lead to boot problems and prevent your system from starting correctly. In such cases, you can repair it using an installation USB drive.

______________________________________________________________________

### Repairing the Windows Bootloader

1. Start the Windows Installation Medium
1. Open Command Prompt
1. Run the following commands to reinstall the Windows bootloader

______________________________________________________________________

Launch the DiskPart utility.

```
diskpart
```

Display a list of all available volumes.

```
list volume
```

Select the EFI partition by replacing "(EFI-PARTITION)" with the actual partition number or name of the EFI partition.

```
select volume (EFI-PARTITION)
```

Assign a temporary drive letter 'S'.

```
assign letter S
```

Exit the DiskPart utility.

```
exit
```

Recreate the Windows bootloader.

```
bcdboot C:\windows /s S:
```

Remove the temporary drive letter 'S'.

```
remove letter S
```
