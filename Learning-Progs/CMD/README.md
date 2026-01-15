# Command Line CRUD Operations

This guide provides comprehensive instructions for performing Create, Read, Update, and Delete operations using the command line interface across different operating systems.

## Table of Contents

- [Windows Command Prompt](#windows-command-prompt)
- [Windows PowerShell](#windows-powershell)
- [Linux/macOS Terminal](#linuxmacos-terminal)

## Windows Command Prompt

### Create Operations

**Create a new file:**
```cmd
echo. > filename.txt
type nul > filename.txt
copy con filename.txt
```

**Create a new directory:**
```cmd
mkdir directory_name
md directory_name
```

**Create multiple directories:**
```cmd
mkdir dir1 dir2 dir3
```

**Write content to a file:**
```cmd
echo Your content here > filename.txt
echo Additional line >> filename.txt
```

### Read Operations

**Display file contents:**
```cmd
type filename.txt
more filename.txt
```

**List files in directory:**
```cmd
dir
dir /b
dir /s
```

**Search within files:**
```cmd
find "search_term" filename.txt
findstr "pattern" filename.txt
```

### Update Operations

**Append to a file:**
```cmd
echo New content >> filename.txt
```

**Replace file content:**
```cmd
echo New content > filename.txt
```

**Rename a file:**
```cmd
ren old_name.txt new_name.txt
rename old_name.txt new_name.txt
```

**Rename a directory:**
```cmd
ren old_directory new_directory
```

**Move a file:**
```cmd
move filename.txt destination_path
```

### Delete Operations

**Delete a file:**
```cmd
del filename.txt
erase filename.txt
```

**Delete multiple files:**
```cmd
del *.txt
del file1.txt file2.txt
```

**Delete a directory:**
```cmd
rmdir directory_name
rd directory_name
```

**Delete directory with contents:**
```cmd
rmdir /s directory_name
rd /s /q directory_name
```

## Windows PowerShell

### Create Operations

**Create a new file:**
```powershell
New-Item -Path "filename.txt" -ItemType File
Out-File -FilePath "filename.txt"
```

**Create a new directory:**
```powershell
New-Item -Path "directory_name" -ItemType Directory
mkdir directory_name
```

**Write content to a file:**
```powershell
Set-Content -Path "filename.txt" -Value "Your content here"
"Your content" | Out-File -FilePath "filename.txt"
```

### Read Operations

**Display file contents:**
```powershell
Get-Content filename.txt
cat filename.txt
type filename.txt
```

**List files in directory:**
```powershell
Get-ChildItem
ls
dir
```

**Search within files:**
```powershell
Select-String -Path "filename.txt" -Pattern "search_term"
```

### Update Operations

**Append to a file:**
```powershell
Add-Content -Path "filename.txt" -Value "New content"
"New content" | Out-File -FilePath "filename.txt" -Append
```

**Replace file content:**
```powershell
Set-Content -Path "filename.txt" -Value "New content"
```

**Rename a file or directory:**
```powershell
Rename-Item -Path "old_name.txt" -NewName "new_name.txt"
ren old_name.txt new_name.txt
```

**Move a file:**
```powershell
Move-Item -Path "filename.txt" -Destination "destination_path"
```

### Delete Operations

**Delete a file:**
```powershell
Remove-Item -Path "filename.txt"
del filename.txt
```

**Delete a directory:**
```powershell
Remove-Item -Path "directory_name"
```

**Delete directory with contents:**
```powershell
Remove-Item -Path "directory_name" -Recurse
Remove-Item -Path "directory_name" -Recurse -Force
```

## Linux/macOS Terminal

### Create Operations

**Create a new file:**
```bash
touch filename.txt
> filename.txt
cat > filename.txt
```

**Create a new directory:**
```bash
mkdir directory_name
```

**Create nested directories:**
```bash
mkdir -p parent/child/grandchild
```

**Write content to a file:**
```bash
echo "Your content here" > filename.txt
cat > filename.txt << EOF
Your content here
EOF
```

### Read Operations

**Display file contents:**
```bash
cat filename.txt
less filename.txt
more filename.txt
head filename.txt
tail filename.txt
```

**List files in directory:**
```bash
ls
ls -la
ls -lh
```

**Search within files:**
```bash
grep "search_term" filename.txt
grep -r "search_term" directory_name
```

### Update Operations

**Append to a file:**
```bash
echo "New content" >> filename.txt
cat >> filename.txt << EOF
New content
EOF
```

**Replace file content:**
```bash
echo "New content" > filename.txt
```

**Rename a file or directory:**
```bash
mv old_name.txt new_name.txt
```

**Move a file:**
```bash
mv filename.txt destination_path/
```

**Copy a file:**
```bash
cp source.txt destination.txt
cp -r source_dir destination_dir
```

### Delete Operations

**Delete a file:**
```bash
rm filename.txt
```

**Delete multiple files:**
```bash
rm file1.txt file2.txt
rm *.txt
```

**Delete a directory:**
```bash
rmdir directory_name
```

**Delete directory with contents:**
```bash
rm -r directory_name
rm -rf directory_name
```

## Common Flags and Options

### Windows Command Prompt

- `/s` - Include subdirectories
- `/q` - Quiet mode, no confirmation
- `/b` - Bare format, filenames only
- `/a` - Display hidden files

### PowerShell

- `-Recurse` - Include subdirectories
- `-Force` - Override restrictions
- `-Confirm` - Prompt before action
- `-WhatIf` - Preview without executing

### Linux/macOS

- `-r` or `-R` - Recursive operation
- `-f` - Force operation without confirmation
- `-i` - Interactive mode, prompt before action
- `-v` - Verbose output
- `-a` - Include hidden files

## Best Practices

1. Always verify the path before executing delete operations
2. Use interactive mode when deleting important files
3. Create backups before performing bulk update operations
4. Use version control systems for critical files
5. Test commands with non-critical files first
6. Be cautious with wildcard characters in delete operations

## Notes

- Commands may require administrative privileges for certain operations
- Path separators differ between Windows (backslash) and Unix-like systems (forward slash)
- Some commands have multiple aliases for convenience

- Error messages should be reviewed carefully before retrying operations
