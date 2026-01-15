# Creating `.md` Files in PowerShell (pwsh)

You can **create a `.md` (Markdown) file** directly in PowerShell using built-in cmdlets.

---

## 1. Using `New-Item` cmdlet

```powershell
New-Item filename.md
```

**Example:**

```powershell
New-Item README.md
```

* Creates an empty Markdown file named `README.md` in the current directory.

---

## 2. Using `Set-Content` to add content while creating

```powershell
Set-Content filename.md "# Title"
```

**Example:**

```powershell
Set-Content README.md "# Project Title"
```

* Creates a Markdown file and adds `# Project Title` as the first line.

---

## 3. Using `Out-File`

```powershell
"# Title" | Out-File filename.md
```

**Example:**

```powershell
"# Project Title" | Out-File README.md
```

* Another method to create a file and write initial content.

---

## 4. Using full paths

```powershell
New-Item C:\Users\Username\Documents\README.md
```

* Creates the file in a specific location.

---

## Notes

* You can open `.md` files after creation using any editor (Notepad, VS Code, etc.).
* PowerShell cmdlets are object-based and more versatile than CMD commands.
* To overwrite content, use `Set-Content`; to append content, use `Add-Content`.


