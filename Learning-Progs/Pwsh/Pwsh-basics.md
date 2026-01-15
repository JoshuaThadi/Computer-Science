# PowerShell (pwsh) CRUD Operations Guide

This document explains how to perform **CRUD (Create, Read, Update, Delete)** operations using **PowerShell (pwsh)**. PowerShell is a powerful, object-oriented command-line shell and scripting language used for automation, system administration, and development workflows.

---

## What is CRUD?

CRUD stands for:

* **Create** – Create files or directories
* **Read** – View file contents or list files and directories
* **Update** – Modify existing files
* **Delete** – Remove files or directories

---

## PowerShell Basics

* `pwsh` is the modern, cross-platform version of PowerShell.
* Commands in PowerShell are called **cmdlets**.
* Cmdlets follow the format: `Verb-Noun` (example: `Get-Content`).

---

# CRUD Operations in PowerShell

## 1. Create

### Create a file

```powershell
New-Item file.txt
```

### Create a directory

```powershell
New-Item myfolder -ItemType Directory
```

---

## 2. Read

### View file contents

```powershell
Get-Content file.txt
```

### List files and directories

```powershell
Get-ChildItem
```

### List files in a specific directory

```powershell
Get-ChildItem myfolder
```

---

## 3. Update

### Edit a file using Notepad

```powershell
notepad file.txt
```

### Append text to a file

```powershell
Add-Content file.txt "New content"
```

### Overwrite file content

```powershell
Set-Content file.txt "Updated content"
```

---

## 4. Delete

### Delete a file

```powershell
Remove-Item file.txt
```

### Delete an empty directory

```powershell
Remove-Item myfolder
```

### Delete a directory with contents

```powershell
Remove-Item myfolder -Recurse -Force
```

---

# Move Files and Folders in PowerShell

## Syntax

```powershell
Move-Item source destination
```

## Move a file to a folder

```powershell
Move-Item file.txt myfolder
```

## Move using full paths

```powershell
Move-Item C:\Users\Username\Desktop\file.txt C:\Users\Username\Documents\myfolder
```

## Rename while moving

```powershell
Move-Item file.txt myfolder\newname.txt
```

## Move multiple files

```powershell
Move-Item *.txt myfolder
```

---

# Copy Files and Folders

### Copy a file

```powershell
Copy-Item file.txt myfolder
```

### Copy a directory with contents

```powershell
Copy-Item myfolder backupfolder -Recurse
```

---

## Notes

* PowerShell works with objects, not plain text.
* Use `-Recurse` carefully as it affects all subdirectories and files.
* Use `-Force` to remove hidden or read-only items.
* Administrator privileges may be required for protected paths.

---

## Conclusion

PowerShell provides a robust and consistent way to manage files and directories through CRUD operations. Mastering these cmdlets improves automation capabilities, system administration efficiency, and development workflows across platforms.
