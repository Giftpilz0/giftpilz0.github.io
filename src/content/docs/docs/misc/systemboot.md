---
title: Windows Boot Problems
---

On UEFI systems the firmware loads the Windows Boot Manager (`\EFI\Microsoft\Boot\bootmgfw.efi`) from the small EFI
system partition (ESP). It reads the boot configuration (BCD) next to it and starts Windows from the `C:` partition. If the ESP or BCD is damaged, Windows itself is
usually fine and only the boot files need to be recreated.

```mermaid
flowchart LR
  uefi[UEFI] --> esp["EFI partition<br/>Boot Manager + BCD"]
  esp --> winload["C:<br/>winload.efi"]
  winload --> windows[Windows]
```

## Repairing the bootloader

1. Boot from a Windows installation USB drive.

1. Press <kbd>Shift</kbd>+<kbd>F10</kbd> on the first setup screen to open a command prompt.

1. Find the partitions and give the ESP a drive letter:

   ```bat
   diskpart
   list volume
   select volume 3
   assign letter=S
   exit
   ```

   The ESP is the small (100–500 MB) `FAT32` volume, often labelled _System_. Also note the letter of the Windows volume:
   in the installer it is not always `C:`.

1. Recreate the boot files and BCD, with the Windows volume as the source:

   ```bat
   bcdboot C:\Windows /s S: /f UEFI
   ```

1. Restart without the USB drive.

The temporary letter `S:` disappears on restart, so `remove letter=S` in `diskpart` is optional.

:::tip
If `bcdboot` reports a failure, check the source path with `dir C:\Windows`. On a BitLocker-encrypted volume, unlock it
first with `manage-bde -unlock C: -RecoveryPassword <key>`.
:::
