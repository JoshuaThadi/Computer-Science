# Creating `.md` Files from CMD

## 1. Using `type` command

```cmd
type nul > filename.md
```

**Example:**

```cmd
type nul > README.md
```

* Creates an empty Markdown file named `README.md` in the current directory.

---

## 2. Using `echo` command

```cmd
echo # Title > filename.md
```

**Example:**

```cmd
echo # Project Title > README.md
```

* Creates a Markdown file and adds `# Project Title` as the first line.

---

## 3. Using `copy con` command

```cmd
copy con filename.md
```

**Example:**

```cmd
copy con README.md
```

* Allows you to type content directly into the file.
* Press `Ctrl + Z` and then `Enter` to save and exit.

---

## 4. Using full paths

```cmd
type nul > C:\Users\Username\Documents\README.md
```

* Creates the file in a specific location.

---

## Notes

* After creation, you can open `.md` files using any editor, e.g., Notepad, VS Code.
* These methods work on **Windows CMD**. For **PowerShell**, `New-Item filename.md` is recommended.


