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
