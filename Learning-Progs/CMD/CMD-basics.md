# CRUD Operations Using Command Line (CMD / Terminal)

This document explains how to perform **CRUD (Create, Read, Update, Delete)** operations using the command line. These operations are commonly used for managing files and directories in development, scripting, and system administration.

---

## What is CRUD?

CRUD stands for:

* **Create** – Create files or directories
* **Read** – View file contents or list directories
* **Update** – Modify existing files
* **Delete** – Remove files or directories

---

# Windows Command Prompt (CMD)

## 1. Create

### Create a file

```cmd
type nul > file.txt
```

### Create a directory

```cmd
mkdir myfolder
```

---

## 2. Read

### View file contents

```cmd
type file.txt
```

### List files and folders

```cmd
dir
```

---

## 3. Update

### Edit a file using Notepad

```cmd
notepad file.txt
```

### Append text to a file

```cmd
echo New content >> file.txt
```

---

## 4. Delete

### Delete a file

```cmd
del file.txt
```

### Delete an empty directory

```cmd
rmdir myfolder
```

### Delete a directory with contents

```cmd
rmdir /s myfolder
```

---

# Linux / macOS Terminal (Bash)

## 1. Create

### Create a file

```bash
touch file.txt
```

### Create a directory

```bash
mkdir myfolder
```

---

## 2. Read

### View file contents

```bash
cat file.txt
```

### List files and directories

```bash
ls
```

---

## 3. Update

### Edit a file using nano

```bash
nano file.txt
```

### Append text to a file

```bash
echo "New content" >> file.txt
```

---

## 4. Delete

### Delete a file

```bash
rm file.txt
```

### Delete an empty directory

```bash
rmdir myfolder
```

### Delete a directory with contents

```bash
rm -r myfolder
```

---

## Notes

* Use delete commands carefully as they permanently remove files.
* Administrative or sudo permissions may be required for protected files.
* These commands are foundational for scripting, DevOps, and backend development workflows.

---

## Conclusion

CRUD operations using the command line are essential skills for developers and system administrators. Mastering these commands improves efficiency and provides better control over file system management.


---


### Move a file to a folder using Command Prompt (Windows CMD)

#### Syntax

```cmd
move source_file destination_folder
```

#### Example

Move `file.txt` to a folder named `myfolder`:

```cmd
move file.txt myfolder
```

#### Move with full paths

```cmd
move C:\Users\Username\Desktop\file.txt C:\Users\Username\Documents\myfolder
```

#### Rename while moving

```cmd
move file.txt myfolder\newname.txt
```

#### Move multiple files

```cmd
move *.txt myfolder
```

#### If the folder does not exist

```cmd
mkdir myfolder
move file.txt myfolder
```

**Notes**

* If a file with the same name exists, CMD will ask for confirmation.
* Use absolute paths to avoid location errors.
* `move` works for both files and folders.

### Copy and Paste Files and Folders in Command Prompt (CMD)

---

## Copy Files in CMD

### Copy a single file

```cmd
copy source_file destination
```

**Example**

```cmd
copy file.txt myfolder
```

---

### Copy and rename a file

```cmd
copy file.txt myfolder\newname.txt
```

---

### Copy multiple files

```cmd
copy *.txt myfolder
```

---

### Copy a file using full paths

```cmd
copy C:\Users\Username\Desktop\file.txt C:\Users\Username\Documents\myfolder
```

---

## Copy Folders in CMD

CMD does **not** support copying folders using `copy`.
Use `xcopy` or `robocopy`.

---

### Copy a folder using `xcopy`

```cmd
xcopy source_folder destination_folder /E /I
```

**Example**

```cmd
xcopy myfolder backupfolder /E /I
```

**Flags explanation**

* `/E` → Copies all subfolders (including empty ones)
* `/I` → Assumes destination is a directory

---

### Copy a folder using `robocopy` (recommended)

```cmd
robocopy source_folder destination_folder /E
```

**Example**

```cmd
robocopy myfolder backupfolder /E
```

---

## Copy a Folder with Files Only

```cmd
xcopy myfolder backupfolder /S /I
```

---

## Notes

* `copy` → Files only
* `xcopy` → Files and folders (older but common)
* `robocopy` → Best for large folders and reliability
* CMD does not have a separate paste command; copy operations include the destination path.


